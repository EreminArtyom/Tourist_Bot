import sqlite3
connection = sqlite3.connect('C:\\Users\\Artem\\PyCharm\\MyDataBase\\TouristBotStatistics_new.db')
cursor = connection.cursor()
Loc=[
    [
        'Форт № 1 Штайн',#Название
        'Калининград, Пос. Большое Исаково, ориентир — Бауцентр на Московском проспекте, 1-й съезд',#адесс
        'самый первый из 15 фортов оборонительного кольца города-крепости Кёнигсберг',#Описание
        'https://visit-kaliningrad.ru/guestcard/fort-1-shtayn/',#Ссылка на сайт
        10,#Cкидка
        'klgd',
        'kult',
        'AgACAgIAAxkBAAILX2Yz9EMlwtY3_Z6xEHGX1DxFs_e8AAJx2zEbizygSdqpkLbNSlfXAQADAgADeAADNAQ'

    ],[
        'ТУРИСТИЧЕСКАЯ ФИРМА «КОРОЛЕВСКИЙ ЗАМОК»',#Название#
        'Калининград, Ленинский пр. 81, гостиница «КАЛИНИНГРАД», 1-й этаж, холл',#адесс
        'экскурсии по Калининраду и области',#Описание
        'https://visit-kaliningrad.ru/guestcard/turisticheskaya-firma-korolevskiy-zamok/',#Ссылка на сайт
        7,#Cкидка
        'klgd',
        'tur',
        'AgACAgIAAxkBAAILYGYz9Kp5cUL-JyOzbAKwp02xBWDgAAKO2zEbizygSW6PB3rNPMIuAQADAgADeQADNAQ'
    ],[
        'ТУРИСТИЧЕСКАЯ ФИРМА «ЮНОНА»',#Название#
        'Калининград, г. Калининград, ул. Октябрьская, 8, головной офис - ул. Октябрьская , д. 57',#адесс
        'индивидуальные и групповые  экскурсии, сборные туры в Калининградскую область',#Описание
        'https://visit-kaliningrad.ru/guestcard/turisticheskaya-firma-yunona/',#Ссылка на сайт
        5,#Cкидка
        'klgd',
        'tur',
        'AgACAgIAAxkBAAILYWYz9Mk6pjgEhpnY-hVtlgXKi7Q4AAKP2zEbizygSVYpDwYDIYllAQADAgADeAADNAQ'
    ],[
        'ТУРИСТИЧЕСКАЯ ФИРМА "ЦВЕТ ПРОГУЛКИ"',#Название#
        'Калининград, Проспект Мира, д. 108',#адесс
        'групповые и индивидуальные авторские экскурсии в малых группах по Калининградской области с нескучными гидами',#Описание
        'https://visit-kaliningrad.ru/guestcard/turisticheskaya-firma-tsvet-tur/',#Ссылка на сайт
        7,#Cкидка
        'klgd',
        'tur',
        'AgACAgIAAxkBAAILYmYz9OSkSthvwyKJ1JGUxma2LlqZAAKT2zEbizygSa4EvHQZXTqrAQADAgADeAADNAQ'
    ],
    [
        'ФОРТ №11 "ДЁНХОФ"',#Название
        'Калининград, Энергетиков, 12',#адесс
        'форт, в котором проводятся экскурсии каждый час с 11 до 17 часов только по выходным и в праздничные дни.',#Описание
        'https://visit-kaliningrad.ru/guestcard/fort-11-dyenkhof/',#Ссылка на сайт
        10,#Cкидка
        'klgd',
        'kult',
        'AgACAgIAAxkBAAILY2Yz9P05fTYJC6spFhQmWVyVVz4sAAKU2zEbizygSadSAbOQDmOoAQADAgADeAADNAQ'
    ],
    [
        'КАЛИНИНГРАДСКИЙ ОБЛАСТНОЙ МУЗЕЙ ИЗОБРАЗИТЕЛЬНЫХ ИСКУССТВ',#Название
        'Калининград, Ленинский проспект, д. 83',#адесс
        'единственный в регионе универсальный музей национального и зарубежного изобразительного искусства.',#Описание
        'https://visit-kaliningrad.ru/guestcard/kaliningradskiy-oblastnoy-muzey-izobrazitelnykh-iskusstv/',#Ссылка на сайт
        10,#Cкидка
        'klgd',
        'kult',
        'AgACAgIAAxkBAAILZGYz9RGOyWa_7LLMYNu3D1PbxYwuAAKV2zEbizygSTGW2Mwk3wkfAQADAgADeAADNAQ'
    ],
    [
        'ПИВОВАРНЯ PONARTH (ПОНАРТ)',#Название
        'Калининград, Киевский переулок, 1',#адесс
        'пивоварный завод, в котором проводям авторские экскурсии на современное производство Ponarth.',#Описание
        'https://visit-kaliningrad.ru/guestcard/pivovarnya-ponarth-ponart/',#Ссылка на сайт
        15,#Cкидка
        'klgd',
        'ent',
        'AgACAgIAAxkBAAILZWYz9SzNhVZmATnaI6yR_N57XYX2AAKY2zEbizygSbX4tZOQj_suAQADAgADeQADNAQ'
    ],
    [
        'КАФЕ-ЛАВКА "ХОМЛИНЫ"',#Название
        'Калининград, ул. Степана Разина, 24',#адесс
        'кафе, в котором представлено уникальное авторское меню, реализованное  по мотивам книги «Хомлины в поисках дома».',#Описание
        'https://visit-kaliningrad.ru/guestcard/masterskaya-khomlinov_2/',#Ссылка на сайт
        10,#Cкидка
        'klgd',
        'food',
        'AgACAgIAAxkBAAILZmYz9T5QWHt_HiTReJGQO91SIdeYAAKa2zEbizygSRs6dA9ANmiUAQADAgADeAADNAQ'
    ],
    [
        'МАГАЗИН ОДЕЖДЫ "MOLINIALIFE" (МОЛИНИЯ ЛАЙФ)',#Название
        'Калининград, ТРЦ «Балтия Молл», магазин Molinialife, Гурьевский район, Приморское кольцо,2',#адесс
        'магазин одежды, где продают нескучные сувениры для воспоминаний о Калининграде  - шопперы, салфетки, стеганные пледы.',#Описание
        'https://visit-kaliningrad.ru/guestcard/magazin-odezhdy-moliniya-layf-molinialife-/',#Ссылка на сайт
        5,#Cкидка
        'klgd',
        'suv',
        'AgACAgIAAxkBAAILZ2Yz9Vzt2HU-nSjxxLkfS3kIYPOxAAKb2zEbizygSWyRrMch1mJjAQADAgADeAADNAQ'
    ],
    [
        'ГАСТРОЛАВКА "БУРРАТА"',#Название
        'Калининград, ул. Карла Маркса, 16 (цокольный этаж)',#адесс
        'магазин, основанный владельцами сыроварни "Cheesarium".',#Описание
        'https://visit-kaliningrad.ru/guestcard/gastrolavka-burrata/',#Ссылка на сайт
        5,#Cкидка
        'klgd',
        'food',
        'AgACAgIAAxkBAAILaGYz9XhrQLDbDWROhpZd1tyZclKPAAKc2zEbizygSX244ItJjN53AQADAgADeAADNAQ'
    ],
    [
        'МАГАЗИН ЯНТАРНОЙ КОСМЕТИКИ "AMBERICA" (АМБЕРИКА)',#Название
        'Калининград, ул. Театральная, 30 (ТРЦ "Европа", 1 этаж); остров Канта (напротив кафе "Булочки Канта"); Площадь Победы, 10 (ТРЦ "Кловер"); Аэропорт "Храброво" (1 и 2 этаж)',#адесс
        'ведущий бренд янтарной косметики с  в Калининградской области.',#Описание
        'https://visit-kaliningrad.ru/guestcard/magazin-yantarnoy-kosmetiki-amberica/',#Ссылка на сайт
        5,#Cкидка
        'klgd',
        'suv',
        'AgACAgIAAxkBAAILaWYz9Y5YdZI7fMcEdOT3v1qGzHCFAAKp2zEbizygSYTFwBFmuJzdAQADAgADeAADNAQ'
    ],
    [
        'КАФЕ "ТРДЕЛЬНИК"',#Название
        'Калининград, Проспект Мира, 1 (напротив КГТУ)',#адесс
        'кафе, где продаётся трдельник - традиционная чешская выпечка в форме цилиндра.',#Описание
        'https://visit-kaliningrad.ru/guestcard/trdelnik-v-kaliningrade/',#Ссылка на сайт
        10,#Cкидка
        'klgd',
        'food',
        'AgACAgIAAxkBAAILamYz9alZ8VeR2P4ayaM1GR_QZ9CNAAKr2zEbizygSXPcdKTrlmTDAQADAgADeQADNAQ'
    ],
    [
        'МУЗЕЙ «ЛЕГЕНДЫ СТАРОГО ГОРОДА»',#Название
        'Калининград, Астрономический бастион, Гвардейский проспект, 22',#адесс
        'музей-театр, расположен в самом центре города Калининграда.',#Описание
        'https://visit-kaliningrad.ru/guestcard/muzey-legendy-starogo-goroda/',#Ссылка на сайт
        10,#Cкидка
        'klgd',
        'kult',
        'AgACAgIAAxkBAAILa2Yz9di8vMZmJtHBA1qeNT3AKavAAAKu2zEbizygSSJz56GX487AAQADAgADeAADNAQ'
    ],
    [
        'МУЗЕЙНОЕ ПРОСТРАНСТВО «РАТСХОФХАУС»',#Название
        'Калининград, ул. Харьковская, д. 71 (вход со двора)',#адесс
        'частный музей «Ратсхофхаус» в длинном-длинном доме с долгой историей в старинном районе Кёнигсберга.',#Описание
        'https://visit-kaliningrad.ru/guestcard/muzeynoe-prostranstvo-ratskhofkhaus/',#Ссылка на сайт
        20,#Cкидка
        'klgd',
        'kult',
        'AgACAgIAAxkBAAILbGYz9e2wcLwzTdnRW50uv05O23_LAAKw2zEbizygSeINPYJWAeLjAQADAgADeAADNAQ'
    ],
    [
        'КАФЕ "BRAVO ITALIA" (БРАВО ИТАЛИЯ)',#Название
        'Калининград, Правая набережная, 9к2',#адесс
        'итальянское кафе на набережной Преголи.',#Описание
        'https://visit-kaliningrad.ru/guestcard/kafe-bravo-italia-bravo-italiya/',#Ссылка на сайт
        15,#Cкидка
        'klgd',
        'food',
        'AgACAgIAAxkBAAILbWYz9gABkrKdry5z9q7wt_qh_dTolQACs9sxG4s8oEl4o4AXXvk7VgEAAwIAA3gAAzQE'
    ],
    [
        'ЯНТАРНАЯ И НАТУРАЛЬНАЯ КОСМЕТИКА "SPRING"',#Название
        'Калининград, Советский проспект, 8',#адесс
        'компания, которая производит качественную янтарную косметику для жителей и гостей нашей области.',#Описание
        'https://visit-kaliningrad.ru/guestcard/yantarnaya-i-naturalnaya-kosmetika-spring/',#Ссылка на сайт
        10,#Cкидка
        'klgd',
        'suv',
        'AgACAgIAAxkBAAILbmYz9ikOcbxJXGEguUkAAaMb8TLwuwACtNsxG4s8oEmmMt5PfSt93QEAAwIAA3gAAzQE'
    ],
    [
        'ПАБ-РЕСТОРАН "ДЖЕНТЛМЕНЫ"',#Название
        'Калининград, ул. Октябрьская, 12 (Рыбная Деревня)',#адесс
        'бар, находящийся в популярном среди жителей и гостей Калининграда квартале Рыбная деревня.',#Описание
        'https://visit-kaliningrad.ru/guestcard/pab-restoran-dzhentlmeny-/',#Ссылка на сайт
        10,#Cкидка
        'klgd',
        'food',
        'AgACAgIAAxkBAAILb2Yz9jw0krPzMWJy5PslJQGLJ9ZsAAK22zEbizygSQdNtzaG5KHkAQADAgADeAADNAQ'
    ],
    [
        'РЕСТОРАН - ПИВОВАРНЯ "ХМЕЛЬ"',#Название
        'Калининград, Площадь Победы, 10',#адесс
        'пивоварня, где продают традиционные блюда русской и сибирской кухни, приготовленные из деликатесов.',#Описание
        'https://visit-kaliningrad.ru/guestcard/restoran-pivovarnya-khmel/',#Ссылка на сайт
        10,#Cкидка
        'klgd',
        'food',
        'AgACAgIAAxkBAAILcGYz9lj0HcvSi7blUjpqQRFAX9d0AAK32zEbizygSZ3FlwR9VGeqAQADAgADeAADNAQ'
    ],
    [
        'АВТОПРОКАТ "PAVLOV"',#Название
        'Калининград, ул. Юрия Гагарина, 116',#адесс
        'автопрокат с самым большим выбором автомобилей.',#Описание
        'https://visit-kaliningrad.ru/guestcard/arenda-avtomobiley-pavlov/',#Ссылка на сайт
        10,#Cкидка
        'klgd',
        'driv',
        'AgACAgIAAxkBAAILcWYz9nQzNVqbIl06V2Y4d2hdN6CyAAK42zEbizygSWkF4ivLkRAVAQADAgADeAADNAQ'
    ],
    [
        'АРЕНДА АПАРТАМЕНТОВ PAVLOV',#Название
        'Калининград, У озера; у вокзала; у парка; у академии',#адесс
        'апартаменты с великолепными местоположением и дизайнерским решением.',#Описание
        'https://visit-kaliningrad.ru/guestcard/arenda-apartamentov-pavlov/',#Ссылка на сайт
        10,#Cкидка
        'klgd',
        'liv',
        'AgACAgIAAxkBAAILcmYz9orcUYxK4YMPzy6mDjWC2gsfAAK52zEbizygSa_HQyCq_g3rAQADAgADeAADNAQ'
    ],
    [
        'ПЕРВЫЙ РЫБНЫЙ РЕСТОРАН "СОЛНЕЧНЫЙ КАМЕНЬ"',#Название
        'Калининград, пл. Маршала Василевского, 3',#адесс
        'ресторан с уютной атмосферой с оттенком средневекового интерьера.',#Описание
        'https://visit-kaliningrad.ru/guestcard/restoran-solnechnyy-kamen-/',#Ссылка на сайт
        10,#Cкидка
        'klgd',
        'food',
        'AgACAgIAAxkBAAILc2Yz9qbm0OASE5X7vxi__lt63d5hAAK62zEbizygScAjdOFs-c47AQADAgADeAADNAQ'
    ],
    [
        'МАГАЗИН СУВЕНИРОВ "РЫЖАЯ ЗАРЯ"',#Название
        'Калининград, Ленинский пр-т, 20; Аэропорт "Храброво"',#адесс
        'сувенирный магазин, в котором вы можете сделать себе или своим близким приятный подарок.',#Описание
        'https://visit-kaliningrad.ru/guestcard/ryzhaya-zarya/',#Ссылка на сайт
        4,#Cкидка
        'klgd',
        'suv',
        'AgACAgIAAxkBAAILdGYz9rykZJV0HdeRGalbKmsL5UDxAAK72zEbizygSUgAAfFG42WumAEAAwIAA3gAAzQE'
    ],
    [
        'РЕСТОРАН "KAISER WURST" (КАЙЗЕРВУРСТ)',#Название
        'Калининград, ул. Театральная, д. 30, ТРЦ "Европа" атриум Берлин, 3-ий этаж',#адесс
        'ресторан Кёнигсбергской кухни, в котором есть лучшие блюда Восточной Пруссии по оригинальным рецептам.',#Описание
        'https://visit-kaliningrad.ru/guestcard/restoran-kaiser-wurst/',#Ссылка на сайт
        10,#Cкидка
        'klgd',
        'food',
        'AgACAgIAAxkBAAILdWYz9tVFozciDpbpaNgP_7D9Cf70AAK-2zEbizygSQahNNjT6PfJAQADAgADeAADNAQ'
    ],
    [
        'ТЕРМАЛЬНЫЙ КОМПЛЕКС "ПЛЯЖ ПОСЕЙДОН"',#Название
        'Калининград, Верхнее озеро, ул. Пролетарская набережная (ориентир – отель «Mercure»)',#адесс
        'термальный комплекс, предлагающий гостям множество услуг.',#Описание
        'https://visit-kaliningrad.ru/guestcard/plyazhnyy-kompleks-poseydon/',#Ссылка на сайт
        15,#Cкидка
        'klgd',
        'SPA',
        'AgACAgIAAxkBAAILdmYz9uotPow0H5RIsF4-Uxp-CZrSAAK_2zEbizygSRjchSBzrLjrAQADAgADeAADNAQ'
    ],
    [
        'МУЗЕЙ МИРОВОГО ОКЕАНА',#Название
        'Калининград, Набережная Петра Великого, д. 1',#адесс
        'единственный в России комплексный морской музей, первый в Калининградской области музей-заповедник.',#Описание
        'https://visit-kaliningrad.ru/guestcard/muzey-mirovogo-okeana/',#Ссылка на сайт
        10,#Cкидка
        'klgd',
        'kult',
        'AgACAgIAAxkBAAILd2Yz9v3vrxSMm7F9apHIW8GcgHkpAALB2zEbizygSa3TwiLqrZj0AQADAgADeAADNAQ'
    ],
    [
        'ПРОКАТ КАТАМАРАНОВ "ПОСЕЙДОН"',#Название
        'Калининград, ул. Пролетарская, 98',#адесс
        'прокат, который предложить вам водные прогулки на катамаранах в центре города.',#Описание
        'https://visit-kaliningrad.ru/guestcard/prokat-katamaranov-poseydon/',#Ссылка на сайт
        10,#Cкидка
        'klgd',
        'driv',
        'AgACAgIAAxkBAAILeGYz9xw9gHxy4yxVWQ-pumEdwlAlAALC2zEbizygSYW2_zp9lbfPAQADAgADeAADNAQ'
    ],
    [
        'КАЛИНИНГРАДСКИЙ ОБЛАСТНОЙ ИСТОРИКО-ХУДОЖЕСТВЕННЫЙ МУЗЕЙ',#Название
        'Калининград, ул. Клиническая, 21',#адесс
        'старейший музей региона, музей, с которого начинается Калининград.',#Описание
        'https://visit-kaliningrad.ru/guestcard/kaliningradskiy-oblastnoy-istoriko-khudozhestvennyy-muzey/',#Ссылка на сайт
        10,#Cкидка
        'klgd',
        'kult',
        'AgACAgIAAxkBAAILeWYz9zLLsohTbwW84aSrOYyb5Ft3AALD2zEbizygSU8_tO7otjE5AQADAgADeAADNAQ'
    ],
    [
        'ТУРИСТИЧЕСКАЯ ФИРМА "УНИВЕРСАЛ-ТУР"',#Название
        'Калининград, 1-ый офис - Советский пр-кт. 36Б; 2-ой офис - ул. Октябрьская, д. 29А',#адесс
        'одни из лидеров на рынке туристических услуг Калининградской области.',#Описание
        'https://visit-kaliningrad.ru/guestcard/universal-tur_kaliningrad/',#Ссылка на сайт
        10,#Cкидка
        'klgd',
        'tur',
        'AgACAgIAAxkBAAILemYz90QHgnKahOh-w1qQkCwjaaI4AALE2zEbizygSag0FeEIJ8CNAQADAgADeAADNAQ'
    ],
    [
        'САЛОН "AMBER SEA"',#Название
        'Калининград, Ленинский пр-т, д. 29',#адесс
        'мир света и мягких тёплых бликов натурального балтийского янтаря.',#Описание
        'https://visit-kaliningrad.ru/guestcard/universal-tur_kaliningrad/',#Ссылка на сайт
        10,#Cкидка
        'klgd',
        'suv',
        'AgACAgIAAxkBAAILe2Yz91o-W-IlVRA8XlmdKR7PfiBzAALF2zEbizygSQxYipGzostsAQADAgADeAADNAQ'
    ],
    [
        'МУЗЕЙ ЯНТАРЯ',#Название
        'Калининград, Площадь Маршала Василевского, д.1',#адесс
        'единственный в России Музей янтаря.',#Описание
        'https://visit-kaliningrad.ru/guestcard/muzey-yantarya/',#Ссылка на сайт
        3,#Cкидка
        'klgd',
        'kult',
        'AgACAgIAAxkBAAILfGYz93CvkeydPSmBYMd0cjQxRRGtAALG2zEbizygSV9pIe9XCMrIAQADAgADeAADNAQ'
    ],
    [
        'ТУРИСТИЧЕСКАЯ ФИРМА «ЮНОНА»',#Название
        'Зеленоградск, г. Зеленоградск, ул. Курортный проспект, 21',#адесс
        'фирма, которая неоднократно признавалась лучшим туроператором по экскурсионному туризму.',#Описание
        'https://visit-kaliningrad.ru/guestcard/turisticheskaya-firma-yunona_zel/',#Ссылка на сайт
        5,#Cкидка
        'zel',
        'tur',
        'AgACAgIAAxkBAAILfWYz94abJhmkgp9PbjrwG1ZStBRJAAKP2zEbizygSVYpDwYDIYllAQADAgADeAADNAQ'
    ],
    [
        'МАГАЗИН ЯНТАРНОЙ КОСМЕТИКИ "AMBERICA" (АМБЕРИКА)',#Название
        'Зеленоградск, Курортный проспект, 22; Национальный парк "Куршская коса" (37,3 км)',#адесс
        'ведущий бренд янтарной косметики в Калининградской области.',#Описание
        'https://visit-kaliningrad.ru/guestcard/magazin-yantarnoy-kosmetiki-amberica-amberika/',#Ссылка на сайт
        5,#Cкидка
        'zel',
        'suv',
        'AgACAgIAAxkBAAILfmYz95wPmxvdaRR1s4lgl0lCuxdgAALH2zEbizygSdPzCTFMIZQyAQADAgADeAADNAQ'
    ],
    [
        'БРЕНД «AMBERIAS JEWELRY»',#Название
        'Зеленоградск, ул. Горького, 2',#адесс
        'бренд, создающий современные и стильные минималистичные украшения.',#Описание
        'https://visit-kaliningrad.ru/guestcard/brend-amberias-jewelry-/',#Ссылка на сайт
        7,#Cкидка
        'zel',
        'suv',
        'AgACAgIAAxkBAAILf2Yz97DGm7cDn7uOvUjm6PcXETLXAALL2zEbizygSY_5Ra7wARehAQADAgADeAADNAQ'
    ],
    [
        'ГРЦ «ПАРАDOX»',#Название
        'Зеленоградск, ул. Саратовская, 2а',#адесс
        'центр, который предлагает гостям города посещение музеев и боулинг-клуба.',#Описание
        'https://visit-kaliningrad.ru/guestcard/grts-paradox/',#Ссылка на сайт
        10,#Cкидка
        'zel',
        'kult',
        'AgACAgIAAxkBAAILgGYz98re8slmrdbozD2XEHOg0jhGAALM2zEbizygSZE0QiZvaHCGAQADAgADeAADNAQ'
    ],
    [
        'АВТОПРОКАТ "PAVLOV"',#Название
        'Зеленоградск, Променад',#адесс
        'автопрокат с самым большим выбором автомобилей.',#Описание
        'https://visit-kaliningrad.ru/guestcard/arenda-avtomobiley-pavlov5567_zelenogradsk/',#Ссылка на сайт
        10,#Cкидка
        'zel',
        'driv',
        'AgACAgIAAxkBAAILgWYz993n7_Z7Q0rwEYG1spRqvdfXAAK42zEbizygSWkF4ivLkRAVAQADAgADeAADNAQ'
    ],
    [
        'ТУРИСТИЧЕСКАЯ ФИРМА «ПЛАНЕТА»',#Название
        'Светлогорск, ул. Ленина, 33, строение 1',#адесс
        'фирма, которая организует приём и размещение туристов в отелях, санаториях и частном секторе Светлогорска.',#Описание
        'https://visit-kaliningrad.ru/guestcard/planeta/',#Ссылка на сайт
        10,#Cкидка
        'sve',
        'tur',
        'AgACAgIAAxkBAAILgmYz9_MzB_NVLhh43tCjzv4Rd1oMAALN2zEbizygSWBSAgaGgTrWAQADAgADeAADNAQ'
    ],
    [
        'ДОМ-МУЗЕЙ ГЕРМАНА БРАХЕРТА',#Название
        'Светлогорск, ул. Токарева, 7',#адесс
        'музей, в экспозиции которого представлены подлинные произведения мастера.',#Описание
        'https://visit-kaliningrad.ru/guestcard/dom-muzey-germana-brakherta/',#Ссылка на сайт
        20,#Cкидка
        'sve',
        'kult',
        'AgACAgIAAxkBAAILg2Yz-AqAAAEw2DZ1eKm4zYqirbZ95wACztsxG4s8oEnKZqV1HuJzQgEAAwIAA3gAAzQE'
    ],
    [
        'ТУРИСТИЧЕСКАЯ ФИРМА "УНИВЕРСАЛ-ТУР"',#Название
        'Светлогорск, ул. Ленина д. 33 А',#адесс
        'одни из лидеров на рынке туристических услуг Калининградской области.',#Описание
        'https://visit-kaliningrad.ru/guestcard/turisticheskaya-firma-universal-tur/',#Ссылка на сайт
        10,#Cкидка
        'sve',
        'tur',
        'AgACAgIAAxkBAAILhGYz-CAJxqL1rf_T56jNCA4Gge3fAALE2zEbizygSag0FeEIJ8CNAQADAgADeAADNAQ'
    ],
    [
        'МОРСКОЙ ВЫСТАВОЧНЫЙ ЦЕНТР МУЗЕЯ МИРОВОГО ОКЕАНА',#Название
        'Светлогорск, ул. Ленина, 11 (1 этаж Театра эстрады «Янтарь-Холл»)',#адесс
        'выставочный центр, где экспонируется уникальная этнографическая коллекция «Люди моря».',#Описание
        'https://visit-kaliningrad.ru/guestcard/muzey-mirovogo-okeana5160_svetlogorsk/',#Ссылка на сайт
        10,#Cкидка
        'sve',
        'kult',
        'AgACAgIAAxkBAAILhWYz-DhswKn0uFWGI6XfjbFjKAbbAALP2zEbizygSRzcrsBrB4SNAQADAgADeAADNAQ'
    ],
    [
        'САЛОН "AMBER SEA"',#Название
        'Янтарный, ул. Дачная, 10',#адесс
        'мир света и мягких тёплых бликов натурального балтийского янтаря.',#Описание
        'https://https://visit-kaliningrad.ru/guestcard/salon-amber-sea_yantaniy/',#Ссылка на сайт
        10,#Cкидка
        'yant',
        'suv',
        'AgACAgIAAxkBAAILhmYz-EqBHBO1mw4LbhXiNW-rYIK8AALQ2zEbizygSQTxb-r-AVj-AQADAgADeAADNAQ'
    ],
    [
        'СТАРЫЙ МАЯК В ПОС. ЗАЛИВИНО НА БЕРЕГУ КУРШСКОГО ЗАЛИВА',#Название
        'Полесск, пос. Заливино, ул. Причальная',#адесс
        'историко-ландшафтный комплекс, принадлежащий Музею Мирового океана.',#Описание
        'https://visit-kaliningrad.ru/guestcard/mayak-rinderort-v-posyelke-zalivino/',#Ссылка на сайт
        10,#Cкидка
        'pol',
        'kult',
        'AgACAgIAAxkBAAILh2Yz-GHtyvzMd3Frcx1UR0JIvmepAALR2zEbizygSV53B3QmbWECAQADAgADeAADNAQ'
    ],
    [
        'ЦЕНТР ОТДЫХА "АНГЕЛ"',#Название
        'Черняховск, 92 км. Гусевского шоссе, Черняховский район, Калининградской области',#адесс
        'центр отдыха, содержащий 14 комфортабельных номеров различных категорий.',#Описание
        'https://visit-kaliningrad.ru/guestcard/zagorodnyy-park-otel-angel/',#Ссылка на сайт
        10,#Cкидка
        'cher',
        'liv',
        'AgACAgIAAxkBAAILiGYz-Hdto5qL3dYcZEYLSvBXCQm1AALS2zEbizygSeFfYcBKUfFrAQADAgADeAADNAQ'
    ]
]
def CityCode(s):
    if s == 'klgd':
        return('Калининград ')
    if s == 'zel':
        return('Зеленоградск')
    if s == 'sve':
        return('Светлогорск ')
    if s == 'yant':
        return('Янтарный    ')
    if s == 'pol':
        return('Полесск     ')
    if s == 'cher':
        return('Черняховск  ')
def default_data():
    cursor.execute('DELETE FROM visit WHERE count > -1')
    connection.commit()
    for p in Loc:
        cursor.execute('INSERT INTO visit (location, city, count) VALUES (?, ?, ?)', (p[0]+' '+CityCode(p[5]), p[5], 0))
        connection.commit()
    i = 0
    cursor.execute('DELETE FROM places WHERE id > -1')
    connection.commit()
    for p in Loc:
        cursor.execute('INSERT INTO places (id, Pic, Name, Address, desc, link, sale, City, type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (i, p[7], p[0], p[1], p[2], p[3], p[4], p[5], p[6]))
        connection.commit()
        i += 1
    cursor.execute('DELETE FROM rating WHERE rtng > -1')
    connection.commit()
    for j in range(1, 6):
        cursor.execute('INSERT INTO rating (rtng, number) VALUES (?, ?)', (j, 0))
        connection.commit()
default_data()
connection.close()
