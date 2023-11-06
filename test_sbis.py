def test_case_1(browser):
    '''
    Sbis page tests:
    1) Открыть https://sbis.ru/ и перейти в раздел Контакты
    2) Найти баннер Тензор и перейти по его ссылке
    3) На странице https://tensor.ru/ проверить наличие 
       блока "Сила в людях"
    4) Перейти в этом блоке в "Подробнее" и убедится, что открывается
       https://tensor.ru/about
    5) Находим раздел Работаем и проверяем, что у всех фотографии
       хронологии одинаковые высота (height) и ширина (width)
    '''

    # 1) Открыть https://sbis.ru/ и перейти в раздел Контакты
    contact_button = browser.get_contacts_button()
    assert contact_button is not None
    browser.click_on_it_js(contact_button)

    #  2) Найти баннер Тензор и перейти по его ссылке
    tenzor_banner = browser.get_tenzor_banner()
    assert tenzor_banner is not None
    browser.click_on_it_js(tenzor_banner)

    #  3) На странице https://tensor.ru/ проверить наличие
    #     блока "Сила в людях"
    browser.switch_windows(-1)
    p = browser.get_p_text()
    assert p.text == 'Сила в людях'

    # 4) Перейти в этом блоке в "Подробнее" и убедится, что открывается
    #    https://tensor.ru/about
    about_link = browser.get_about_link()
    browser.click_on_it_js(about_link)
    browser.switch_windows(-1)
    page_url = browser.get_url()
    assert page_url == 'https://tensor.ru/about'

   #  5) Находим раздел Работаем и проверяем, что у всех фотографии
   #     хронологии одинаковые высота (height) и ширина (width)
    images = browser.get_images()
    img_width = [img.size['width'] for img in images]
    img_heigth = [img.size['height'] for img in images]
    assert len(set(img_width)) == 1
    assert len(set(img_heigth)) == 1

def test_case_2(browser):
    '''
    Sbis page tests:
    1) Перейти на https://sbis.ru/ в раздел "Контакты"
    2) Проверить, что определился ваш регион (в нашем примере
    Ярославская обл.) и есть список партнеров.
    3) Изменить регион на Камчатский край
    4) Проверить, что подставился выбранный регион, список партнеров
    изменился, url и title содержат информацию выбранного региона
    '''
    
   #  1) Перейти на https://sbis.ru/ в раздел "Контакты"
    browser.switch_windows(0)

   #  2) Проверить, что определился ваш регион (в нашем примере
   #  Ярославская обл.) и есть список партнеров.
    area = browser.get_area()
    page_title = browser.get_title()
    assert area.text == 'Свердловская обл.'
    assert page_title == 'СБИС Контакты — Свердловская область'
    partners = browser.get_partrers()
    assert partners is not None
    page_url = browser.get_url()

    #  3) Изменить регион на Камчатский край
    browser.click_on_it(area)
    new_area = browser.choose_area()
    browser.click_on_it(new_area)

    #  4) Проверить, что подставился выбранный регион, список партнеров
    #  изменился, url и title содержат информацию выбранного региона
    area = browser.get_area()
    page_title_new = browser.get_title()
    assert area.text == 'Камчатский край'
    assert page_title_new != page_title
    partners_new_area = browser.get_partrers()
    assert partners != partners_new_area
    page_url_new_area = browser.get_url()
    assert page_url != page_url_new_area
    new_area = page_title_new.split(' — ')[1]
    assert new_area == 'Камчатский край'
