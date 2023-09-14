
class pageutil:
    def __init__(self) -> None:
        pass
    def getpageindex(self,pagecount,page,pageindex):
        if page <=5:
            return page-1
        if pagecount - page >= 2:
            pageindex = 4
            return pageindex
        if pagecount - page < 2:
            return pageindex +1
        



if __name__ == "__main__":

    page = pageutil()

    pageindex = page.getpageindex(11,2,4)

    print(pageindex)