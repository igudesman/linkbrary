class Link:
    def __init__(self, title=None, url=None, viewed=None, topics=None, estimated_time=None, dict_params=None):
        if title is None:
            self.title = 'sample title'
        else:
            self.title = title
        if url is None:
            self.url = 'no url :c'
        else:
            self.url = url
        if viewed is None:
            self.viewed = False
        else:
            self.viewed = viewed
        if topics is None:
            self.topics = []
        else:
            self.topics = topics
        if estimated_time is None:
            self.estimated_time = 'N/A'
        else:
            self.estimated_time = estimated_time
        if dict_params is not None:
            # construct from a dictionary
            for key, value in dict_params.items():
                setattr(self, key, value)

    def __str__(self):
        return f'{self.url}\n' \
               f'Topics: _{self.topics}_\n' \
               f'Estimated time: {self.estimated_time} min.'
