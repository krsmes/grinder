# The Grinder 3.5
# HTTP script recorded by TCPProxy at Sep 5, 2011 2:19:04 PM

from net.grinder.script import Test
from net.grinder.script.Grinder import grinder
from net.grinder.plugin.http import HTTPPluginControl, HTTPRequest
from HTTPClient import NVPair
connectionDefaults = HTTPPluginControl.getConnectionDefaults()
httpUtilities = HTTPPluginControl.getHTTPUtilities()

# To use a proxy server, uncomment the next line and set the host and port.
# connectionDefaults.setProxyServer("localhost", 8001)

# These definitions at the top level of the file are evaluated once,
# when the worker process is started.

connectionDefaults.defaultHeaders = \
  [ NVPair('Accept-Language', 'en-us,en;q=0.5'),
    NVPair('Accept-Charset', 'UTF-8,*'),
    NVPair('Accept-Encoding', 'gzip, deflate'),
    NVPair('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:6.0.1) Gecko/20100101 Firefox/6.0.1'), ]

headers0= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'), ]

headers1= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'),
    NVPair('Referer', 'http://www.google.com/'), ]

headers2= \
  [ NVPair('Accept', '*/*'),
    NVPair('Referer', 'http://www.google.com/'), ]

headers3= \
  [ NVPair('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    NVPair('Referer', 'http://www.google.com/'), ]

headers4= \
  [ NVPair('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5'), ]

url0 = 'http://www.google.com:80'
url1 = 'http://lh6.googleusercontent.com:80'
url2 = 'http://ssl.gstatic.com:80'
url3 = 'http://news.google.com:80'
url4 = 'http://id.google.com:80'

# Create an HTTPRequest for each request, then replace the
# reference to the HTTPRequest with an instrumented version.
# You can access the unadorned instance using request101.__target__.
# Open Google
request101 = HTTPRequest(url=url0, headers=headers0)
request101 = Test(101, 'GET /').wrap(request101)

request102 = HTTPRequest(url=url0, headers=headers1)
request102 = Test(102, 'GET nav_logo83.png').wrap(request102)

request103 = HTTPRequest(url=url0, headers=headers1)
request103 = Test(103, 'GET logo3w.png').wrap(request103)

request104 = HTTPRequest(url=url0, headers=headers1)
request104 = Test(104, 'GET usflag-transbg_42.png').wrap(request104)

request105 = HTTPRequest(url=url0, headers=headers2)
request105 = Test(105, 'GET onfG_zsPY5Q.js').wrap(request105)

request201 = HTTPRequest(url=url1, headers=headers1)
request201 = Test(201, 'GET photo.jpg').wrap(request201)

request301 = HTTPRequest(url=url2, headers=headers1)
request301 = Test(301, 'GET h_bedf916a.png').wrap(request301)

request401 = HTTPRequest(url=url0, headers=headers3)
request401 = Test(401, 'GET get').wrap(request401)

request402 = HTTPRequest(url=url0, headers=headers2)
request402 = Test(402, 'GET 3830b863ea014d9f.js').wrap(request402)

request403 = HTTPRequest(url=url0, headers=headers1)
request403 = Test(403, 'GET swxa.gif').wrap(request403)

request501 = HTTPRequest(url=url0, headers=headers1)
request501 = Test(501, 'GET csi').wrap(request501)

request601 = HTTPRequest(url=url2, headers=headers2)
request601 = Test(601, 'GET smm_4e7ed55e11b990b80650522c8d97e615.js').wrap(request601)

# Search for grinder
request701 = HTTPRequest(url=url0, headers=headers3)
request701 = Test(701, 'GET s').wrap(request701)

request801 = HTTPRequest(url=url0, headers=headers3)
request801 = Test(801, 'GET s').wrap(request801)

request901 = HTTPRequest(url=url0, headers=headers3)
request901 = Test(901, 'GET s').wrap(request901)

request1001 = HTTPRequest(url=url0, headers=headers3)
request1001 = Test(1001, 'GET s').wrap(request1001)

request1101 = HTTPRequest(url=url0, headers=headers3)
request1101 = Test(1101, 'GET s').wrap(request1101)

request1201 = HTTPRequest(url=url0, headers=headers3)
request1201 = Test(1201, 'GET s').wrap(request1201)

request1202 = HTTPRequest(url=url0, headers=headers1)
request1202 = Test(1202, 'GET red_icons_sm_A_J_dot.png').wrap(request1202)

request1301 = HTTPRequest(url=url0, headers=headers1)
request1301 = Test(1301, 'GET data=Ay5GWBeob_WIPLDYoIWcfVXxvZu9XwJ55OX7Ag,s1rwsVlHAh8RxMJ5i_YJHNu_zhrExd-BCItp-QjDYVsl3KmNazqnZR_vVcpPCiiolyEHqeNG0ZR5ypvln_zjdohpgXtADwt0PhUX0Jhy6823ORFrGPJ5tmdznWIp_u2ob6TvZwNFcKJcUZzoMATWmSiT3V4jkNv5fF20gIBw_nRVwWAAtTSMnQvqWsMK70ZBs5SPW568uSJJy0djxNQ42ArMHHf5HNRiDCICosWkmrPVbN7wVi-NEkjOd-p-CWSKnncf0hg').wrap(request1301)

request1302 = HTTPRequest(url=url0, headers=headers2)
request1302 = Test(1302, 'GET L-0Dy2P5c0o.js').wrap(request1302)

request1401 = HTTPRequest(url=url0, headers=headers3)
request1401 = Test(1401, 'GET search').wrap(request1401)

request1501 = HTTPRequest(url=url0, headers=headers2)
request1501 = Test(1501, 'GET data=L6F5Ck3rk0DOPylyywxsg9iVtTzTyYTijaklq6XVuKej94Xm-Q-kILfxMYciSQ,s1rwsVlHAh8RxMJ5i_YJHNu_zhrExd-BCItp-QjDYVsl3KmNazqnZR_vVcpPCiiolyEHqeNG0ZR5ypvln_zjdohpgXtADwt0PhUX0Jhy6823ORFrGPJ5tmdznWIp_u2ob6TvZwNFcKJcUZzoMATWmSiT3V4jkNv5fF20gIBw_nRVwWAAtTSMnQvqWsMK70ZBs5SPW568uSJJy0djxNQ42ArMHHf5HNRiDCICosWkmrPVbN7wVi-NEkjOd-p-CWSKnncf0hg&callback=google.LU.loadFeaturemap_726_0').wrap(request1501)

request1601 = HTTPRequest(url=url0, headers=headers1)
request1601 = Test(1601, 'GET gen_204').wrap(request1601)

request1701 = HTTPRequest(url=url3, headers=headers1)
request1701 = Test(1701, 'GET GYsAOPHMvo8J').wrap(request1701)

request1801 = HTTPRequest(url=url4, headers=headers4)
request1801 = Test(1801, 'GET EAAAAL2rssKo-zB1YMgIqKApDYE.gif').wrap(request1801)

request1901 = HTTPRequest(url=url0, headers=headers1)
request1901 = Test(1901, 'GET csi').wrap(request1901)

request1902 = HTTPRequest(url=url0, headers=headers2)
request1902 = Test(1902, 'GET L-0Dy2P5c0o.js').wrap(request1902)


class TestRunner:
  """A TestRunner instance is created for each worker thread."""

  # A method for each recorded page.
  def page1(self):
    """GET / (requests 101-105)."""
    result = request101.GET('/')

    grinder.sleep(400)
    request102.GET('/images/nav_logo83.png')

    request103.GET('/intl/en_com/images/srpr/logo3w.png')

    request104.GET('/images/icons/hpcg/usflag-transbg_42.png')

    grinder.sleep(127)
    request105.GET('/extern_js/f/CgJlbhICdXMrMEU4ACwrMFo4ACwrMA44ACwrMBc4ACwrMDw4ACwrMFE4ACwrMFk4ACwrMJgBOAAsKzAKOABAiwGaAgJjYywrMBY4ACwrMBk4ACwrMCE4AJoCBHRpbmcsKzAlOAAsKzAqOAAsKzArOAAsKzA1OAAsKzBBOAAsKzBNOAAsKzBOOAAsKzBTOACaAgZzZWFyY2gsKzBUOAAsKzBfOACaAidtb3ZlX2NhY2hlX3NpbWlsYXJfaW50b192aXN1YWxfc25pcHBldHMsKzBiOAAsKzBjOAAsKzBpOAAsKzBzOAAsKzB4OAAsKzCKATgALCswkgE4ACwrMKwBOAAsKzB0OAAsKzB9OAAsKzAdOAAsKzBcOACaAgJjYywrMG84ACwrMBg4ACwrMCY4ACyAAlOQAk0/onfG_zsPY5Q.js')

    return result

  def page2(self):
    """GET photo.jpg (request 201)."""
    result = request201.GET('/-VH8hC1MFzwA/AAAAAAAAAAI/AAAAAAAAAAA/6ZUQQsCO2vo/s24-c/photo.jpg')

    return result

  def page3(self):
    """GET h_bedf916a.png (request 301)."""
    result = request301.GET('/gb/images/h_bedf916a.png')

    return result

  def page4(self):
    """GET get (requests 401-403)."""
    self.token_hl = \
      'en'
    self.token_gl = \
      'us'
    self.token_authuser = \
      '0'
    self.token_bundleJs = \
      '0'
    result = request401.GET('/ig/cp/get' +
      '?hl=' +
      self.token_hl +
      '&gl=' +
      self.token_gl +
      '&authuser=' +
      self.token_authuser +
      '&bundleJs=' +
      self.token_bundleJs)

    request402.GET('/extern_chrome/3830b863ea014d9f.js')

    request403.GET('/images/swxa.gif')

    return result

  def page5(self):
    """GET csi (request 501)."""
    self.token_v = \
      '3'
    self.token_s = \
      'webhp'
    self.token_action = \
      ''
    self.token_e = \
      '28936,30316,30465,30541,31215,31632,31916,31922,32532'
    self.token_ei = \
      'tBJlTozdCNDpgQeuwvRt'
    self.token_expi = \
      '28936,30316,30465,30541,31215,31632,31916,31922,32532'
    self.token_imc = \
      '5'
    self.token_imn = \
      '5'
    self.token_imp = \
      '0'
    self.token_rt = \
      'xjsls.218,prt.231,xjses.4296,xjsee.4326,xjs.4337,ol.4720,iml.231'
    result = request501.GET('/csi' +
      '?v=' +
      self.token_v +
      '&s=' +
      self.token_s +
      '&action=' +
      self.token_action +
      '&e=' +
      self.token_e +
      '&ei=' +
      self.token_ei +
      '&expi=' +
      self.token_expi +
      '&imc=' +
      self.token_imc +
      '&imn=' +
      self.token_imn +
      '&imp=' +
      self.token_imp +
      '&rt=' +
      self.token_rt)

    return result

  def page6(self):
    """GET smm_4e7ed55e11b990b80650522c8d97e615.js (request 601)."""
    result = request601.GET('/gb/js/smm_4e7ed55e11b990b80650522c8d97e615.js')

    return result

  def page7(self):
    """GET s (request 701)."""
    self.token_sugexp = \
      'gsis,i18n=true'
    self.token_cp = \
      '1'
    self.token_gs_id = \
      '4'
    self.token_xhr = \
      't'
    self.token_q = \
      'g'
    self.token_pf = \
      'p'
    self.token_sclient = \
      'psy'
    self.token_site = \
      ''
    self.token_source = \
      'hp'
    self.token_pbx = \
      '1'
    self.token_oq = \
      ''
    self.token_aq = \
      ''
    self.token_aqi = \
      ''
    self.token_aql = \
      ''
    self.token_gs_sm = \
      ''
    self.token_gs_upl = \
      ''
    self.token_bav = \
      'on.2,or.r_gc.r_pw.r_cp.'
    self.token_fp = \
      '3830b863ea014d9f'
    self.token_biw = \
      '1275'
    self.token_bih = \
      '897'
    self.token_tch = \
      '1'
    self.token_ech = \
      '1'
    self.token_psi = \
      'tBJlTozdCNDpgQeuwvRt.1315246776571.1'
    result = request701.GET('/s' +
      '?hl=' +
      self.token_hl +
      '&sugexp=' +
      self.token_sugexp +
      '&cp=' +
      self.token_cp +
      '&gs_id=' +
      self.token_gs_id +
      '&xhr=' +
      self.token_xhr +
      '&q=' +
      self.token_q +
      '&pf=' +
      self.token_pf +
      '&sclient=' +
      self.token_sclient +
      '&site=' +
      self.token_site +
      '&source=' +
      self.token_source +
      '&pbx=' +
      self.token_pbx +
      '&oq=' +
      self.token_oq +
      '&aq=' +
      self.token_aq +
      '&aqi=' +
      self.token_aqi +
      '&aql=' +
      self.token_aql +
      '&gs_sm=' +
      self.token_gs_sm +
      '&gs_upl=' +
      self.token_gs_upl +
      '&bav=' +
      self.token_bav +
      '&fp=' +
      self.token_fp +
      '&biw=' +
      self.token_biw +
      '&bih=' +
      self.token_bih +
      '&tch=' +
      self.token_tch +
      '&ech=' +
      self.token_ech +
      '&psi=' +
      self.token_psi)

    return result

  def page8(self):
    """GET s (request 801)."""
    self.token_cp = \
      '2'
    self.token_gs_id = \
      '8'
    self.token_q = \
      'gr'
    self.token_ech = \
      '2'
    result = request801.GET('/s' +
      '?hl=' +
      self.token_hl +
      '&sugexp=' +
      self.token_sugexp +
      '&cp=' +
      self.token_cp +
      '&gs_id=' +
      self.token_gs_id +
      '&xhr=' +
      self.token_xhr +
      '&q=' +
      self.token_q +
      '&pf=' +
      self.token_pf +
      '&sclient=' +
      self.token_sclient +
      '&site=' +
      self.token_site +
      '&source=' +
      self.token_source +
      '&pbx=' +
      self.token_pbx +
      '&oq=' +
      self.token_oq +
      '&aq=' +
      self.token_aq +
      '&aqi=' +
      self.token_aqi +
      '&aql=' +
      self.token_aql +
      '&gs_sm=' +
      self.token_gs_sm +
      '&gs_upl=' +
      self.token_gs_upl +
      '&bav=' +
      self.token_bav +
      '&fp=' +
      self.token_fp +
      '&biw=' +
      self.token_biw +
      '&bih=' +
      self.token_bih +
      '&tch=' +
      self.token_tch +
      '&ech=' +
      self.token_ech +
      '&psi=' +
      self.token_psi)

    return result

  def page9(self):
    """GET s (request 901)."""
    self.token_cp = \
      '4'
    self.token_gs_id = \
      'f'
    self.token_q = \
      'grin'
    self.token_ech = \
      '3'
    result = request901.GET('/s' +
      '?hl=' +
      self.token_hl +
      '&sugexp=' +
      self.token_sugexp +
      '&cp=' +
      self.token_cp +
      '&gs_id=' +
      self.token_gs_id +
      '&xhr=' +
      self.token_xhr +
      '&q=' +
      self.token_q +
      '&pf=' +
      self.token_pf +
      '&sclient=' +
      self.token_sclient +
      '&site=' +
      self.token_site +
      '&source=' +
      self.token_source +
      '&pbx=' +
      self.token_pbx +
      '&oq=' +
      self.token_oq +
      '&aq=' +
      self.token_aq +
      '&aqi=' +
      self.token_aqi +
      '&aql=' +
      self.token_aql +
      '&gs_sm=' +
      self.token_gs_sm +
      '&gs_upl=' +
      self.token_gs_upl +
      '&bav=' +
      self.token_bav +
      '&fp=' +
      self.token_fp +
      '&biw=' +
      self.token_biw +
      '&bih=' +
      self.token_bih +
      '&tch=' +
      self.token_tch +
      '&ech=' +
      self.token_ech +
      '&psi=' +
      self.token_psi)

    return result

  def page10(self):
    """GET s (request 1001)."""
    self.token_cp = \
      '5'
    self.token_gs_id = \
      'j'
    self.token_q = \
      'grind'
    self.token_ech = \
      '4'
    result = request1001.GET('/s' +
      '?hl=' +
      self.token_hl +
      '&sugexp=' +
      self.token_sugexp +
      '&cp=' +
      self.token_cp +
      '&gs_id=' +
      self.token_gs_id +
      '&xhr=' +
      self.token_xhr +
      '&q=' +
      self.token_q +
      '&pf=' +
      self.token_pf +
      '&sclient=' +
      self.token_sclient +
      '&site=' +
      self.token_site +
      '&source=' +
      self.token_source +
      '&pbx=' +
      self.token_pbx +
      '&oq=' +
      self.token_oq +
      '&aq=' +
      self.token_aq +
      '&aqi=' +
      self.token_aqi +
      '&aql=' +
      self.token_aql +
      '&gs_sm=' +
      self.token_gs_sm +
      '&gs_upl=' +
      self.token_gs_upl +
      '&bav=' +
      self.token_bav +
      '&fp=' +
      self.token_fp +
      '&biw=' +
      self.token_biw +
      '&bih=' +
      self.token_bih +
      '&tch=' +
      self.token_tch +
      '&ech=' +
      self.token_ech +
      '&psi=' +
      self.token_psi)

    return result

  def page11(self):
    """GET s (request 1101)."""
    self.token_cp = \
      '6'
    self.token_gs_id = \
      'n'
    self.token_q = \
      'grinde'
    self.token_ech = \
      '5'
    result = request1101.GET('/s' +
      '?hl=' +
      self.token_hl +
      '&sugexp=' +
      self.token_sugexp +
      '&cp=' +
      self.token_cp +
      '&gs_id=' +
      self.token_gs_id +
      '&xhr=' +
      self.token_xhr +
      '&q=' +
      self.token_q +
      '&pf=' +
      self.token_pf +
      '&sclient=' +
      self.token_sclient +
      '&site=' +
      self.token_site +
      '&source=' +
      self.token_source +
      '&pbx=' +
      self.token_pbx +
      '&oq=' +
      self.token_oq +
      '&aq=' +
      self.token_aq +
      '&aqi=' +
      self.token_aqi +
      '&aql=' +
      self.token_aql +
      '&gs_sm=' +
      self.token_gs_sm +
      '&gs_upl=' +
      self.token_gs_upl +
      '&bav=' +
      self.token_bav +
      '&fp=' +
      self.token_fp +
      '&biw=' +
      self.token_biw +
      '&bih=' +
      self.token_bih +
      '&tch=' +
      self.token_tch +
      '&ech=' +
      self.token_ech +
      '&psi=' +
      self.token_psi)

    return result

  def page12(self):
    """GET s (requests 1201-1202)."""
    self.token_cp = \
      '7'
    self.token_gs_id = \
      'r'
    self.token_q = \
      'grinder'
    self.token_ech = \
      '6'
    result = request1201.GET('/s' +
      '?hl=' +
      self.token_hl +
      '&sugexp=' +
      self.token_sugexp +
      '&cp=' +
      self.token_cp +
      '&gs_id=' +
      self.token_gs_id +
      '&xhr=' +
      self.token_xhr +
      '&q=' +
      self.token_q +
      '&pf=' +
      self.token_pf +
      '&sclient=' +
      self.token_sclient +
      '&site=' +
      self.token_site +
      '&source=' +
      self.token_source +
      '&pbx=' +
      self.token_pbx +
      '&oq=' +
      self.token_oq +
      '&aq=' +
      self.token_aq +
      '&aqi=' +
      self.token_aqi +
      '&aql=' +
      self.token_aql +
      '&gs_sm=' +
      self.token_gs_sm +
      '&gs_upl=' +
      self.token_gs_upl +
      '&bav=' +
      self.token_bav +
      '&fp=' +
      self.token_fp +
      '&biw=' +
      self.token_biw +
      '&bih=' +
      self.token_bih +
      '&tch=' +
      self.token_tch +
      '&ech=' +
      self.token_ech +
      '&psi=' +
      self.token_psi)

    grinder.sleep(1023)
    request1202.GET('/images/red_icons_sm_A_J_dot.png')

    return result

  def page13(self):
    """GET data=Ay5GWBeob_WIPLDYoIWcfVXxvZu9XwJ55OX7Ag,s1rwsVlHAh8RxMJ5i_YJHNu_zhrExd-BCItp-QjDYVsl3KmNazqnZR_vVcpPCiiolyEHqeNG0ZR5ypvln_zjdohpgXtADwt0PhUX0Jhy6823ORFrGPJ5tmdznWIp_u2ob6TvZwNFcKJcUZzoMATWmSiT3V4jkNv5fF20gIBw_nRVwWAAtTSMnQvqWsMK70ZBs5SPW568uSJJy0djxNQ42ArMHHf5HNRiDCICosWkmrPVbN7wVi-NEkjOd-p-CWSKnncf0hg (requests 1301-1302)."""
    self.token_data = \
      'Ay5GWBeob_WIPLDYoIWcfVXxvZu9XwJ55OX7Ag,s1rwsVlHAh8RxMJ5i_YJHNu_zhrExd-BCItp-QjDYVsl3KmNazqnZR_vVcpPCiiolyEHqeNG0ZR5ypvln_zjdohpgXtADwt0PhUX0Jhy6823ORFrGPJ5tmdznWIp_u2ob6TvZwNFcKJcUZzoMATWmSiT3V4jkNv5fF20gIBw_nRVwWAAtTSMnQvqWsMK70ZBs5SPW568uSJJy0djxNQ42ArMHHf5HNRiDCICosWkmrPVbN7wVi-NEkjOd-p-CWSKnncf0hg'
    result = request1301.GET('/maps/vt/data=' +
      self.token_data)

    grinder.sleep(33)
    request1302.GET('/extern_js/f/CgJlbhICdXMrMEo4ACwrMEs4ACyAAlOQAk2iAgNjZHI/L-0Dy2P5c0o.js')

    return result

  def page14(self):
    """GET search (request 1401)."""
    self.token_oq = \
      'grinder'
    self.token_aq = \
      'f'
    self.token_aqi = \
      'g5'
    self.token_gs_sm = \
      'e'
    self.token_gs_upl = \
      '16865l17744l0l19876l7l6l0l0l0l1l618l1907l2-4.1.0.1l6l0'
    self.token_ech = \
      '1'
    self.token_psi = \
      'tBJlTozdCNDpgQeuwvRt.1315246776571.3'
    result = request1401.GET('/search' +
      '?sclient=' +
      self.token_sclient +
      '&hl=' +
      self.token_hl +
      '&source=' +
      self.token_source +
      '&q=' +
      self.token_q +
      '&pbx=' +
      self.token_pbx +
      '&oq=' +
      self.token_oq +
      '&aq=' +
      self.token_aq +
      '&aqi=' +
      self.token_aqi +
      '&aql=' +
      self.token_aql +
      '&gs_sm=' +
      self.token_gs_sm +
      '&gs_upl=' +
      self.token_gs_upl +
      '&bav=' +
      self.token_bav +
      '&fp=' +
      self.token_fp +
      '&biw=' +
      self.token_biw +
      '&bih=' +
      self.token_bih +
      '&tch=' +
      self.token_tch +
      '&ech=' +
      self.token_ech +
      '&psi=' +
      self.token_psi)

    return result

  def page15(self):
    """GET data=L6F5Ck3rk0DOPylyywxsg9iVtTzTyYTijaklq6XVuKej94Xm-Q-kILfxMYciSQ,s1rwsVlHAh8RxMJ5i_YJHNu_zhrExd-BCItp-QjDYVsl3KmNazqnZR_vVcpPCiiolyEHqeNG0ZR5ypvln_zjdohpgXtADwt0PhUX0Jhy6823ORFrGPJ5tmdznWIp_u2ob6TvZwNFcKJcUZzoMATWmSiT3V4jkNv5fF20gIBw_nRVwWAAtTSMnQvqWsMK70ZBs5SPW568uSJJy0djxNQ42ArMHHf5HNRiDCICosWkmrPVbN7wVi-NEkjOd-p-CWSKnncf0hg&callback=google.LU.loadFeaturemap_726_0 (request 1501)."""
    self.token_data = \
      'L6F5Ck3rk0DOPylyywxsg9iVtTzTyYTijaklq6XVuKej94Xm-Q-kILfxMYciSQ,s1rwsVlHAh8RxMJ5i_YJHNu_zhrExd-BCItp-QjDYVsl3KmNazqnZR_vVcpPCiiolyEHqeNG0ZR5ypvln_zjdohpgXtADwt0PhUX0Jhy6823ORFrGPJ5tmdznWIp_u2ob6TvZwNFcKJcUZzoMATWmSiT3V4jkNv5fF20gIBw_nRVwWAAtTSMnQvqWsMK70ZBs5SPW568uSJJy0djxNQ42ArMHHf5HNRiDCICosWkmrPVbN7wVi-NEkjOd-p-CWSKnncf0hg'
    self.token_callback = \
      'google.LU.loadFeaturemap_726_0'
    result = request1501.GET('/maps/vt/data=' +
      self.token_data +
      '&callback=' +
      self.token_callback)

    return result

  def page16(self):
    """GET gen_204 (request 1601)."""
    self.token_atyp = \
      'i'
    self.token_ct = \
      'lu_featuremap'
    self.token_cad = \
      '176'
    self.token_ei = \
      'yhJlTrqsHOLj0gHko62HCg'
    self.token_zx = \
      '1315246796710'
    result = request1601.GET('/gen_204' +
      '?atyp=' +
      self.token_atyp +
      '&ct=' +
      self.token_ct +
      '&cad=' +
      self.token_cad +
      '&ei=' +
      self.token_ei +
      '&zx=' +
      self.token_zx)

    return result

  def page17(self):
    """GET GYsAOPHMvo8J (request 1701)."""
    result = request1701.GET('/news/tbn/GYsAOPHMvo8J')

    return result

  def page18(self):
    """GET EAAAAL2rssKo-zB1YMgIqKApDYE.gif (request 1801)."""
    result = request1801.GET('/verify/EAAAAL2rssKo-zB1YMgIqKApDYE.gif')

    return result

  def page19(self):
    """GET csi (requests 1901-1902)."""
    self.token_s = \
      'web'
    self.token_ei = \
      'zBJlTvWdJs7pgQfM2by1Cg'
    self.token_cp = \
      'false'
    self.token_pfa = \
      'n.6,ttfc.187,ttlc.0,cbt.20'
    self.token_pfm = \
      'n.6,ttfc.493,ttlc.0,cbt.85'
    self.token_imn = \
      '26'
    self.token_alm = \
      '1'
    self.token_rt = \
      'prt.1100,pprt.1100,ol.1100,jsrt.556,iml.1101'
    result = request1901.GET('/csi' +
      '?v=' +
      self.token_v +
      '&s=' +
      self.token_s +
      '&action=' +
      self.token_action +
      '&ei=' +
      self.token_ei +
      '&e=' +
      self.token_e +
      '&cp=' +
      self.token_cp +
      '&imp=' +
      self.token_imp +
      '&pfa=' +
      self.token_pfa +
      '&pfm=' +
      self.token_pfm +
      '&imn=' +
      self.token_imn +
      '&alm=' +
      self.token_alm +
      '&rt=' +
      self.token_rt)

    request1902.GET('/extern_js/f/CgJlbhICdXMrMEo4ACwrMEs4ACyAAlOQAk2iAgNjZHI/L-0Dy2P5c0o.js')

    return result

  def __call__(self):
    """This method is called for every run performed by the worker thread."""
    self.page1()      # GET / (requests 101-105)
    self.page2()      # GET photo.jpg (request 201)
    self.page3()      # GET h_bedf916a.png (request 301)

    grinder.sleep(3344)
    self.page4()      # GET get (requests 401-403)

    grinder.sleep(139)
    self.page5()      # GET csi (request 501)
    self.page6()      # GET smm_4e7ed55e11b990b80650522c8d97e615.js (request 601)

    grinder.sleep(16361)
    self.page7()      # GET s (request 701)
    self.page8()      # GET s (request 801)
    self.page9()      # GET s (request 901)

    grinder.sleep(71)
    self.page10()     # GET s (request 1001)
    self.page11()     # GET s (request 1101)

    grinder.sleep(45)
    self.page12()     # GET s (requests 1201-1202)
    self.page13()     # GET data=Ay5GWBeob_WIPLDYoIWcfVXxvZu9XwJ55OX7Ag,s1rwsVlHAh8RxMJ5i_YJHNu_zhrExd-BCItp-QjDYVsl3KmNazqnZR_vVcpPCiiolyEHqeNG0ZR5ypvln_zjdohpgXtADwt0PhUX0Jhy6823ORFrGPJ5tmdznWIp_u2ob6TvZwNFcKJcUZzoMATWmSiT3V4jkNv5fF20gIBw_nRVwWAAtTSMnQvqWsMK70ZBs5SPW568uSJJy0djxNQ42ArMHHf5HNRiDCICosWkmrPVbN7wVi-NEkjOd-p-CWSKnncf0hg (requests 1301-1302)

    grinder.sleep(521)
    self.page14()     # GET search (request 1401)
    self.page15()     # GET data=L6F5Ck3rk0DOPylyywxsg9iVtTzTyYTijaklq6XVuKej94Xm-Q-kILfxMYciSQ,s1rwsVlHAh8RxMJ5i_YJHNu_zhrExd-BCItp-QjDYVsl3KmNazqnZR_vVcpPCiiolyEHqeNG0ZR5ypvln_zjdohpgXtADwt0PhUX0Jhy6823ORFrGPJ5tmdznWIp_u2ob6TvZwNFcKJcUZzoMATWmSiT3V4jkNv5fF20gIBw_nRVwWAAtTSMnQvqWsMK70ZBs5SPW568uSJJy0djxNQ42ArMHHf5HNRiDCICosWkmrPVbN7wVi-NEkjOd-p-CWSKnncf0hg&callback=google.LU.loadFeaturemap_726_0 (request 1501)
    self.page16()     # GET gen_204 (request 1601)
    self.page17()     # GET GYsAOPHMvo8J (request 1701)

    grinder.sleep(944)
    self.page18()     # GET EAAAAL2rssKo-zB1YMgIqKApDYE.gif (request 1801)

    grinder.sleep(20)
    self.page19()     # GET csi (requests 1901-1902)


def instrumentMethod(test, method_name, c=TestRunner):
  """Instrument a method with the given Test."""
  unadorned = getattr(c, method_name)
  import new
  method = new.instancemethod(test.wrap(unadorned), None, c)
  setattr(c, method_name, method)

# Replace each method with an instrumented version.
# You can call the unadorned method using self.page1.__target__().
instrumentMethod(Test(100, 'Page 1'), 'page1')
instrumentMethod(Test(200, 'Page 2'), 'page2')
instrumentMethod(Test(300, 'Page 3'), 'page3')
instrumentMethod(Test(400, 'Page 4'), 'page4')
instrumentMethod(Test(500, 'Page 5'), 'page5')
instrumentMethod(Test(600, 'Page 6'), 'page6')
instrumentMethod(Test(700, 'Page 7'), 'page7')
instrumentMethod(Test(800, 'Page 8'), 'page8')
instrumentMethod(Test(900, 'Page 9'), 'page9')
instrumentMethod(Test(1000, 'Page 10'), 'page10')
instrumentMethod(Test(1100, 'Page 11'), 'page11')
instrumentMethod(Test(1200, 'Page 12'), 'page12')
instrumentMethod(Test(1300, 'Page 13'), 'page13')
instrumentMethod(Test(1400, 'Page 14'), 'page14')
instrumentMethod(Test(1500, 'Page 15'), 'page15')
instrumentMethod(Test(1600, 'Page 16'), 'page16')
instrumentMethod(Test(1700, 'Page 17'), 'page17')
instrumentMethod(Test(1800, 'Page 18'), 'page18')
instrumentMethod(Test(1900, 'Page 19'), 'page19')
