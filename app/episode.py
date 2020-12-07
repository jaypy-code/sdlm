from os import path

class Episode:
    Link = ''
    Current = ''
    Last = ''

    def __init__(self, link, current, last):
        self.Link = link
        self.Current = current
        self.Last = last

    def _getFile(self):
        return self.Link.split('/')[-1]

    def _getExtension(self):
        return path.splitext(self._getFile())[1]

    def _getFileName(self):
        return path.splitext(self._getFile())[0]

    def _getLoop(self):
        return (int(self.Current[1:]), int(self.Last[1:]))

    def create(self, episode=0):
        episode = str(episode)
        if(len(episode) == 1):
            episode = "0" + episode
        episode = self.Current[0:1] + episode
        file_name = self._getFileName() + self._getExtension()
        file_name = file_name.replace(self.Current, episode)
        link = self.Link.split('/')
        link[-1] = file_name
        return '/'.join(link)

    def getLinks(self):
        start, end = self._getLoop()
        links = []
        for episode in range(start, end + 1):
            links.append(self.create(episode))
        return links

    def ok(self):
        return self._getFileName().find(self.Current) != -1
