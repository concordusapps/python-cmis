from cmislib.exceptions import UpdateConflictException, ObjectNotFoundException
from os import path
from urllib.parse import quote


def get_or_create_folder(repo, folder):
    """Get a folder object from cmis, or create it if it doesn't exist.
    Similar to the unix command `mkdir -p`."""

    folder = path.normpath(folder)

    try:
        return repo.getObjectByPath(folder)

    except ObjectNotFoundException:
        # Folder doesn't exist.
        pass

    # Iterate through the paths by popping the right-most segment.
    remainder, segment = path.split(folder)
    node = get_or_create_folder(remainder)
    return node.createFolder(segment)


def persist(cmis_folder, fobj, name=None):

    # Set a default filename if one was not provided.
    if name is None:
        name = path.basename(fobj.name)

    name, extension = path.splitext(name)

    # Normalize path.  We don't want to use "+" signs, so escape those first.
    name = quote(name, safe='')

    # Iterate until we can successfully upload the file.
    iteration = 0
    while True:
        filename = '%s_%d%s' % (name, iteration, extension)

        try:
            return cmis_folder.createDocument(
                filename, contentFile=fobj)

        except UpdateConflictException:
            iteration += 1
            fobj.seek(0)


def persist_from_disk(cmis_folder, source, name=None):
    """Upload a document using CMIS without clobbering an existing file.
    This is a convenience function that takes a path instead of a file object.
    """

    if name is None:
        name = path.basename(source)

    # Establish a file handle for the source.
    name, extension = path.splitext(name)
    with open(source, 'rb') as stream:
        return persist(cmis_folder, stream, name)
