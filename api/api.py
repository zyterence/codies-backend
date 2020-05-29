from fastapi import APIRouter
from fastapi.responses import JSONResponse
import requests

from models.site import Site, SitePath, SiteURL
from utils.parsers import parse_swifttips, parse_meituan, parse_iostip, meituan_page
router = APIRouter()


@router.get("/")
async def sites():
    return Site.list()


@router.get(SitePath.NEWS, response_class=JSONResponse)
async def news_list():
    r = requests.get(SiteURL.NEWS.value)
    return r.json()


@router.get(SitePath.IOSTIPS, response_class=JSONResponse)
async def iostip_list():
    r = requests.get(SiteURL.IOSTIPS.value)
    tip_list = parse_iostip(r.text)
    return tip_list


@router.get(SitePath.MEITUAN, response_class=JSONResponse)
def meituan_list():
    r = requests.get(meituan_page())
    r.encoding = r.apparent_encoding
    blog_list = parse_meituan(r.text)
    return blog_list


@router.get(SitePath.SWIFTTIPS, response_class=JSONResponse)
def tips():
    r = requests.get(SiteURL.SWIFTTIPS.value)
    tip_list = parse_swifttips(r.text)
    return tip_list
