
class Collection(list):
    def __getitem__(self, item):
        super(Collection, self).__getitem__(item-1)
