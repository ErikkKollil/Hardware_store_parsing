import requests
import json
import pprint


def get_data():
    cookies = {
        '__lhash_': '16f00c7c3f1214f1b7c108507917211c',
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '2',
        'MVID_2_exp_in_1': '1',
        'MVID_AB_SERVICES_DESCRIPTION': 'var4',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'false',
        'MVID_CART_MULTI_DELETE': 'false',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityCZ_7173',  # Город: Воронеж, CityCZ_975
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GUEST_ID': '20959460591',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '7700000000000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_LOGIN': 'true',
        'MVID_NEW_LK_MENU_BUTTON': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_NEW_SUGGESTIONS': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_REGION_ID': '1',
        'MVID_REGION_SHOP': 'S002',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PICKUP_SEAMLESS_AB_TEST': '2',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'flacktory': 'no',
        'searchType2': '3',
        'MVID_ENVCLOUD': 'primary',
        'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
        'admitad_uid': 'mvideo',
        'utm_term': 'mvideo',
        '__SourceTracker': 'yandex__cpc',
        'admitad_deduplication_cookie': 'yandex__cpc',
        '__cpatrack': 'yandex_cpc',
        '__sourceid': 'yandex',
        '__allsource': 'yandex',
        'SMSError': '',
        'authError': '',
        'partnerSrc': 'yandex',
        '_gid': 'GA1.2.225232898.1656398807',
        '_dc_gtm_UA-1873769-1': '1',
        '_ym_d': '1656398807',
        '_ym_uid': '1656398807949434045',
        'st_uid': 'a322a5d62f7fb656287cc2b7969c5a24',
        'advcake_track_id': '55e1bfc1-e298-512c-654f-563e4d49218b',
        'advcake_utm_partner': 'ipr_Pickup_Image_Name_Pure_search_desktop',
        'advcake_session_id': '40d91a9e-ca25-1620-4f2b-ebc808dda346',
        'advcake_track_url': 'https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dcpc%26utm_campaign%3Dipr_Pickup_Image_Name_Pure_search_desktop%26utm_content%3Dpid%7C21914465604_%7Ccid%7C54501876%7Cgid%7C4285492611%7Caid%7C9547811425%7Cpos%7Cpremium1%7Ckey%7Cmvideo%7Caddphrases%7Cno%7Cdvc%7Cdesktop%7Cregion%7C1107%7Cregion_name%7C%25D0%2590%25D0%25BD%25D0%25B0%25D0%25BF%25D0%25B0%7Ccoef_goal%7C0%7Cdesktop%26utm_term%3Dmvideo%26reff%3Dyandex_cpc_ipr_Pickup_Image_Name_Pure_Search%26etext%3D2202.wgK9QRam3yDeNxDFo-5-1pVNzEeGPZo41r--wKgkzP1laWh2ZnJiaGd3ZGJza2Vv.53e80ade32e0db626e8ae7a4beac19fe6db40d0a%26_openstat%3DZGlyZWN0LnlhbmRleC5ydTs1NDUwMTg3Njs5NTQ3ODExNDI1O3lhbmRleC5ydTpwcmVtaXVt%26yclid%3D3607627010185159678',
        'advcake_utm_webmaster': 'pid%7C21914465604_%7Ccid%7C54501876%7Cgid%7C4285492611%7Caid%7C9547811425%7Cpos%7Cpremium1%7Ckey%7Cmvideo%7Caddphrases%7Cno%7Cdvc%7Cdesktop%7Cregion%7C1107%7Cregion_name%7C%25D0%2590%25D0%25BD%25D0%25B0%25D0%25BF%25D0%25B0%7Ccoef_goal%7C0%7Cdesktop',
        'advcake_click_id': '',
        '_dc_gtm_UA-1873769-37': '1',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': 'c26744e3-4838-431e-bda0-819209904c87',
        '_ym_isad': '2',
        'afUserId': '36c32c13-6b44-4a4e-b6a5-e6c5d863bc01-p',
        'AF_SYNC': '1656398808598',
        'flocktory-uuid': '20c826e0-a5ab-45c8-9c64-3bdd5cac638e-6',
        'adrdel': '1',
        'adrcid': 'A4o2LIheCFF9v7Wlbw5jJKw',
        'BIGipServeratg-ps-prod_tcp80': '2969885706.20480.0000',
        'bIPs': '-971835924',
        'uxs_uid': '1699bfc0-f6ae-11ec-80d7-9d1e8f8bcc7d',
        'wurfl_device_id': 'generic_web_browser',
        'JSESSIONID': 'JGT2v6jcF9VlM1B20v5GH2sV28rFhnqtyBSNxyWqMMv3Fq4ybCBt!-46307858',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        'BIGipServeratg-ps-prod_tcp80_clone': '2969885706.20480.0000',
        'MVID_GTM_BROWSER_THEME': '1',
        'deviceType': 'desktop',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VDUhEfLU0bUllecz1CGiN5a2lUHiNdCGdve2tRJVsoEyoxZnMdSkxaLhw5JmVIDyxvVH8/GjhpI2JHYCdIXT56Kx4XenQrVwgNXEJFX28beyJfKggkYzVfGUNqTg1pN1wUPHVlPkdyeSxEbSViR1olSVE/SF5dSRIyYhJAQE1HDTdAXjdXYTAPFhFNRxU9VlJPQyhrG3FYMA==2Dhb3Q==',
        'cfidsgib-w-mvideo': '+Qr3CgE/X3FXzVIOaT4vPviGPc85CEqDzqs4NHj+Nl4HMdLYWAHA+gZUv0NUGvVD5HJtLBNgrM+4y8zguVAuWnYIdNUzoXubZPt6QPHwUbWLN8GYMNeIt6QY6IQzGc5jkfKE2FhP7aYTokH0rwAaw9B1bPtT1sEAFmnI',
        'gsscgib-w-mvideo': 'uN8CmyMhc8fT+oDw0lB6SYZyORnjZ8jL8qzubT18gHMfXnDbRjmk3u/YLjcUTS1DiHQRzL1TwqakqB//8MbBEQu9sEgVjI9ADKhqBBiYvxSoe8TUSfhuu9hgeGpQl8lJ4dVqf/MBr12kQfvaAzV1fmP4zhc3+9EuJQuJxALYbEdu3B0goloaaDWrnL+OK1WLtmB7bHSqOEnp6COEM03wkbjMprAjnOrjDL+LjXdSddZ4/f7F+36T9eYls9SCWQ==',
        'fgsscgib-w-mvideo': '9E9X63afe2af9520c674bc84c12ea74cb9e8223d',
        'CACHE_INDICATOR': 'false',
        'mindboxDeviceUUID': '71a27418-6fbf-432f-9125-73e0a66ee667',
        'directCrm-session': '%7B%22deviceGuid%22%3A%2271a27418-6fbf-432f-9125-73e0a66ee667%22%7D',
        '_ga': 'GA1.2.1379901543.1656398807',
        '_ga_BNX5WPP3YK': 'GS1.1.1656398807.1.1.1656398859.8',
        '_ga_CFMZTSS5FM': 'GS1.1.1656398806.1.1.1656398859.0',
        'ADRUM_BT': 'R:65|g:66e3ae8e-7836-41ca-8a0f-5c3f84a693001505579',
    }

    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'ru-RU,ru;q=0.9',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '__lhash_=16f00c7c3f1214f1b7c108507917211c; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=2; MVID_2_exp_in_1=1; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_CART_MULTI_DELETE=false; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_975; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GUEST_ID=20959460591; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_LOGIN=true; MVID_NEW_LK_MENU_BUTTON=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_NEW_SUGGESTIONS=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PICKUP_SEAMLESS_AB_TEST=2; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; flacktory=no; searchType2=3; MVID_ENVCLOUD=primary; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; admitad_uid=mvideo; utm_term=mvideo; __SourceTracker=yandex__cpc; admitad_deduplication_cookie=yandex__cpc; __cpatrack=yandex_cpc; __sourceid=yandex; __allsource=yandex; SMSError=; authError=; partnerSrc=yandex; _gid=GA1.2.225232898.1656398807; _dc_gtm_UA-1873769-1=1; _ym_d=1656398807; _ym_uid=1656398807949434045; st_uid=a322a5d62f7fb656287cc2b7969c5a24; advcake_track_id=55e1bfc1-e298-512c-654f-563e4d49218b; advcake_utm_partner=ipr_Pickup_Image_Name_Pure_search_desktop; advcake_session_id=40d91a9e-ca25-1620-4f2b-ebc808dda346; advcake_track_url=https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dcpc%26utm_campaign%3Dipr_Pickup_Image_Name_Pure_search_desktop%26utm_content%3Dpid%7C21914465604_%7Ccid%7C54501876%7Cgid%7C4285492611%7Caid%7C9547811425%7Cpos%7Cpremium1%7Ckey%7Cmvideo%7Caddphrases%7Cno%7Cdvc%7Cdesktop%7Cregion%7C1107%7Cregion_name%7C%25D0%2590%25D0%25BD%25D0%25B0%25D0%25BF%25D0%25B0%7Ccoef_goal%7C0%7Cdesktop%26utm_term%3Dmvideo%26reff%3Dyandex_cpc_ipr_Pickup_Image_Name_Pure_Search%26etext%3D2202.wgK9QRam3yDeNxDFo-5-1pVNzEeGPZo41r--wKgkzP1laWh2ZnJiaGd3ZGJza2Vv.53e80ade32e0db626e8ae7a4beac19fe6db40d0a%26_openstat%3DZGlyZWN0LnlhbmRleC5ydTs1NDUwMTg3Njs5NTQ3ODExNDI1O3lhbmRleC5ydTpwcmVtaXVt%26yclid%3D3607627010185159678; advcake_utm_webmaster=pid%7C21914465604_%7Ccid%7C54501876%7Cgid%7C4285492611%7Caid%7C9547811425%7Cpos%7Cpremium1%7Ckey%7Cmvideo%7Caddphrases%7Cno%7Cdvc%7Cdesktop%7Cregion%7C1107%7Cregion_name%7C%25D0%2590%25D0%25BD%25D0%25B0%25D0%25BF%25D0%25B0%7Ccoef_goal%7C0%7Cdesktop; advcake_click_id=; _dc_gtm_UA-1873769-37=1; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=c26744e3-4838-431e-bda0-819209904c87; _ym_isad=2; afUserId=36c32c13-6b44-4a4e-b6a5-e6c5d863bc01-p; AF_SYNC=1656398808598; flocktory-uuid=20c826e0-a5ab-45c8-9c64-3bdd5cac638e-6; adrdel=1; adrcid=A4o2LIheCFF9v7Wlbw5jJKw; BIGipServeratg-ps-prod_tcp80=2969885706.20480.0000; bIPs=-971835924; uxs_uid=1699bfc0-f6ae-11ec-80d7-9d1e8f8bcc7d; wurfl_device_id=generic_web_browser; JSESSIONID=JGT2v6jcF9VlM1B20v5GH2sV28rFhnqtyBSNxyWqMMv3Fq4ybCBt!-46307858; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; BIGipServeratg-ps-prod_tcp80_clone=2969885706.20480.0000; MVID_GTM_BROWSER_THEME=1; deviceType=desktop; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VDUhEfLU0bUllecz1CGiN5a2lUHiNdCGdve2tRJVsoEyoxZnMdSkxaLhw5JmVIDyxvVH8/GjhpI2JHYCdIXT56Kx4XenQrVwgNXEJFX28beyJfKggkYzVfGUNqTg1pN1wUPHVlPkdyeSxEbSViR1olSVE/SF5dSRIyYhJAQE1HDTdAXjdXYTAPFhFNRxU9VlJPQyhrG3FYMA==2Dhb3Q==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VDUhEfLU0bUllecz1CGiN5a2lUHiNdCGdve2tRJVsoEyoxZnMdSkxaLhw5JmVIDyxvVH8/GjhpI2JHYCdIXT56Kx4XenQrVwgNXEJFX28beyJfKggkYzVfGUNqTg1pN1wUPHVlPkdyeSxEbSViR1olSVE/SF5dSRIyYhJAQE1HDTdAXjdXYTAPFhFNRxU9VlJPQyhrG3FYMA==2Dhb3Q==; cfidsgib-w-mvideo=+Qr3CgE/X3FXzVIOaT4vPviGPc85CEqDzqs4NHj+Nl4HMdLYWAHA+gZUv0NUGvVD5HJtLBNgrM+4y8zguVAuWnYIdNUzoXubZPt6QPHwUbWLN8GYMNeIt6QY6IQzGc5jkfKE2FhP7aYTokH0rwAaw9B1bPtT1sEAFmnI; cfidsgib-w-mvideo=+Qr3CgE/X3FXzVIOaT4vPviGPc85CEqDzqs4NHj+Nl4HMdLYWAHA+gZUv0NUGvVD5HJtLBNgrM+4y8zguVAuWnYIdNUzoXubZPt6QPHwUbWLN8GYMNeIt6QY6IQzGc5jkfKE2FhP7aYTokH0rwAaw9B1bPtT1sEAFmnI; gsscgib-w-mvideo=uN8CmyMhc8fT+oDw0lB6SYZyORnjZ8jL8qzubT18gHMfXnDbRjmk3u/YLjcUTS1DiHQRzL1TwqakqB//8MbBEQu9sEgVjI9ADKhqBBiYvxSoe8TUSfhuu9hgeGpQl8lJ4dVqf/MBr12kQfvaAzV1fmP4zhc3+9EuJQuJxALYbEdu3B0goloaaDWrnL+OK1WLtmB7bHSqOEnp6COEM03wkbjMprAjnOrjDL+LjXdSddZ4/f7F+36T9eYls9SCWQ==; gsscgib-w-mvideo=uN8CmyMhc8fT+oDw0lB6SYZyORnjZ8jL8qzubT18gHMfXnDbRjmk3u/YLjcUTS1DiHQRzL1TwqakqB//8MbBEQu9sEgVjI9ADKhqBBiYvxSoe8TUSfhuu9hgeGpQl8lJ4dVqf/MBr12kQfvaAzV1fmP4zhc3+9EuJQuJxALYbEdu3B0goloaaDWrnL+OK1WLtmB7bHSqOEnp6COEM03wkbjMprAjnOrjDL+LjXdSddZ4/f7F+36T9eYls9SCWQ==; fgsscgib-w-mvideo=9E9X63afe2af9520c674bc84c12ea74cb9e8223d; fgsscgib-w-mvideo=9E9X63afe2af9520c674bc84c12ea74cb9e8223d; cfidsgib-w-mvideo=iu1tRmiATqs3lj/RxvfjwmzzDD60qm/cGTClktqngoDMrB4yPnHercCquFMSBh1RIc2TYtTrBPkHCgVQBnfG4H8qFm5VMmRxAr2V1KCiFICjHPnUfiLKPShmW5uTfpFOgcGLQ10NYWlSbT80CY4KmnYr9Bs032WnSTvI; CACHE_INDICATOR=false; mindboxDeviceUUID=71a27418-6fbf-432f-9125-73e0a66ee667; directCrm-session=%7B%22deviceGuid%22%3A%2271a27418-6fbf-432f-9125-73e0a66ee667%22%7D; _ga=GA1.2.1379901543.1656398807; _ga_BNX5WPP3YK=GS1.1.1656398807.1.1.1656398859.8; _ga_CFMZTSS5FM=GS1.1.1656398806.1.1.1656398859.0; ADRUM_BT=R:65|g:66e3ae8e-7836-41ca-8a0f-5c3f84a693001505579',
        'Referer': 'https://www.mvideo.ru/playstation-4327/ps5-igry-22780/f/skidka=da',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.58 (Edition Yx GX)',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Opera GX";v="87"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'x-set-application-id': '980d2d95-5e86-4c32-943a-bfebc9b6e498',
    }

    params = {
        'categoryId': '22780',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()
    products_ids = response.get('body').get('products')

    with open('1_product_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)

    # print(products_ids) #Получили id товаров со скидкой

    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()

    with open('2_items.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    # print(len(response.get('body').get('products'))) # Количество товаров

    # Склеиваем список id в одну строку
    products_ids_str = ','.join(products_ids)

    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()

    with open('3_price.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    items_prices = {}
    material_prices = response.get('body').get('materialPrices')

    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        items_prices[item_id] = {
            'item_basePrice': item_base_price,
            'item_salePrice': item_sale_price,
            'item_total': item_bonus
        }

    with open('4_items_price.json', 'w') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)


def get_result():
    with open('2_items.json') as file:
        product_data = json.load(file)

    with open('4_items_price.json') as file:
        product_price = json.load(file)

    products_data = product_data.get('body').get('products')

    for item in products_data:
        product_id = item.get('productId')

        if product_id in product_price:
            prices = product_price[product_id]

            item['item_base_Price'] = prices.get('item_basePrice')
            item['item_sale_Price'] = prices.get('item_salePrice')
            item['item_bonus'] = prices.get('item_bonus')

    with open('5_result.json', 'w') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)


def base_info():
    info_list = []
    with open('5_result.json') as file:
        product_data = json.load(file)

    for item in product_data:
        item_name = item.get('modelName')
        item_baseprice = item.get('item_base_Price')
        item_saleprice = item.get('item_sale_Price')
        item_bonus = item.get('item_bonus')
        item_spercent = (int(item_saleprice) / int(item_baseprice)) * 100
        info_list.append([item_name, item_baseprice, item_saleprice, round(100 - item_spercent, 2), item_bonus])
    return info_list


if __name__ == "__main__":
    get_data()
    get_result()
    pprint.pprint(base_info())
