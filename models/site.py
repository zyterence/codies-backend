from typing import TypedDict, List
from enum import Enum, unique


class Category(str, Enum):
    POST = "post"
    WEEKLY = "weakly"


class SiteInfo(TypedDict):
    name: str
    url: str
    path: str
    category: Category


class SitePath(str, Enum):
    NEWS = "/news/"
    MEITUAN = "/meituan/"
    IOSTIPS = "/iostips/"
    SWIFTTIPS = "/swifttips/"
    SWIFTARTICALS = "/articles/"
    MAJIDBLOG = "/swiftwithmajid/"
    APPCODA = "/appcoda/"
    OLDDRIVER = "/olddriver/"


class SiteURL(str, Enum):
    NEWS = "https://api.readhub.cn/technews"
    MEITUAN = "https://tech.meituan.com/"
    IOSTIPS = "https://awesome-tips.github.io/iostip/"
    SWIFTTIPS = "https://swiftbysundell.com/tips/"
    SWIFTARTICALS = "https://swiftbysundell.com/articles/"
    MAJIDBLOG = "https://swiftwithmajid.com/"
    APPCODA = "http://digest.appcoda.com/"
    OLDDRIVER = "https://juejin.im/user/5a52075e6fb9a01c9d31b107/posts"


@unique
class Site(Enum):
    news = SiteInfo(name="news",
                    url=SiteURL.NEWS,
                    path=SitePath.NEWS,
                    category=Category.POST)
    meituan = SiteInfo(name="美团技术团队",
                       url=SiteURL.MEITUAN,
                       path=SitePath.MEITUAN,
                       category=Category.POST)
    iostip = SiteInfo(name="知识小集",
                      url=SiteURL.IOSTIPS,
                      path=SitePath.IOSTIPS,
                      category=Category.POST)
    tips = SiteInfo(name="swiftbysundell/tips",
                    url=SiteURL.SWIFTTIPS,
                    path=SitePath.SWIFTTIPS,
                    category=Category.POST)
    articles = SiteInfo(name="swiftbysundell/articles",
                        url=SiteURL.SWIFTARTICALS,
                        path=SitePath.SWIFTARTICALS,
                        category=Category.POST)
    majid = SiteInfo(name="swiftwithmajid",
                     url=SiteURL.MAJIDBLOG,
                     path=SitePath.MAJIDBLOG,
                     category=Category.POST)

    appcoda = SiteInfo(name="AppCoda",
                       url=SiteURL.APPCODA,
                       path=SitePath.APPCODA,
                       category=Category.WEEKLY)
    olddriver = SiteInfo(name="OldDriver",
                         url=SiteURL.OLDDRIVER,
                         path=SitePath.OLDDRIVER,
                         category=Category.WEEKLY)

    @classmethod
    def list(cls):
        return list(cls)
