class FileHelper:
    @staticmethod
    def get_extension(filename):
        """Επιστρέφει την επέκταση αρχείου"""
        return filename.split(".")[-1] if "." \
            in filename else None


print(FileHelper.get_extension("document.pdf"))
print(FileHelper.get_extension("archive.tar.gz"))
print(FileHelper.get_extension("no_extension"))
