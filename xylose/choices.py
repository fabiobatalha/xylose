# encoding: utf-8

ISO639_1_to_2 = {
    'gv': 'glv', 'gu': 'guj', 'gd': 'gla', 'ga': 'gle', 'gn': 'grn',
    'gl': 'glg', 'lg': 'lug', 'lb': 'ltz', 'la': 'lat', 'ln': 'lin',
    'lo': 'lao', 'tt': 'tat', 'tr': 'tur', 'ts': 'tso', 'li': 'lim',
    'lv': 'lav', 'to': 'ton', 'lt': 'lit', 'lu': 'lub', 'tk': 'tuk',
    'th': 'tha', 'ti': 'tir', 'tg': 'tgk', 'te': 'tel', 'ta': 'tam',
    'yi': 'yid', 'yo': 'yor', 'de': 'ger', 'da': 'dan', 'dz': 'dzo',
    'st': 'sot', 'dv': 'div', 'qu': 'que', 'el': 'ell', 'eo': 'epo',
    'en': 'eng', 'zh': 'chi', 'ee': 'ewe', 'za': 'zha', 'mh': 'mah',
    'uk': 'ukr', 'eu': 'eus', 'et': 'est', 'es': 'spa', 'ru': 'rus',
    'rw': 'kin', 'rm': 'roh', 'rn': 'run', 'ro': 'ron', 'bn': 'ben',
    'be': 'bel', 'bg': 'bul', 'ba': 'bak', 'wa': 'wln', 'wo': 'wol',
    'bm': 'bam', 'jv': 'jav', 'bo': 'bod', 'bh': 'bih', 'bi': 'bis',
    'br': 'bre', 'bs': 'bos', 'ja': 'jpn', 'om': 'orm', 'oj': 'oji',
    'ty': 'tah', 'oc': 'oci', 'tw': 'twi', 'os': 'oss', 'or': 'ori',
    'xh': 'xho', 'ch': 'cha', 'co': 'cos', 'ca': 'cat', 'ce': 'che',
    'cy': 'cym', 'cs': 'ces', 'cr': 'cre', 'cv': 'chv', 'cu': 'chu',
    've': 'ven', 'ps': 'pus', 'pt': 'por', 'tl': 'tgl', 'pa': 'pan',
    'vi': 'vie', 'pi': 'pli', 'is': 'isl', 'pl': 'pol', 'hz': 'her',
    'hy': 'hye', 'hr': 'hrv', 'iu': 'iku', 'ht': 'hat', 'hu': 'hun',
    'hi': 'hin', 'ho': 'hmo', 'ha': 'hau', 'he': 'heb', 'mg': 'mlg',
    'uz': 'uzb', 'ml': 'mal', 'mn': 'mon', 'mi': 'mri', 'ik': 'ipk',
    'mk': 'mkd', 'ur': 'urd', 'mt': 'mlt', 'ms': 'msa', 'mr': 'mar',
    'ug': 'uig', 'my': 'mya', 'ki': 'kik', 'aa': 'aar', 'ab': 'abk',
    'ae': 'ave', 'ss': 'ssw', 'af': 'afr', 'tn': 'tsn', 'sw': 'swa',
    'ak': 'aka', 'am': 'amh', 'it': 'ita', 'an': 'arg', 'ii': 'iii',
    'ia': 'ina', 'as': 'asm', 'ar': 'ara', 'su': 'sun', 'io': 'ido',
    'av': 'ava', 'ay': 'aym', 'az': 'aze', 'id': 'ind', 'ig': 'ibo',
    'sk': 'slk', 'sr': 'srp', 'nl': 'nld', 'nn': 'nno', 'no': 'nor',
    'na': 'nau', 'nb': 'nob', 'nd': 'nde', 'ne': 'nep', 'ng': 'ndo',
    'ny': 'nya', 'vo': 'vol', 'zu': 'zul', 'so': 'som', 'nr': 'nbl',
    'nv': 'nav', 'sn': 'sna', 'fr': 'fra', 'sm': 'smo', 'fy': 'fry',
    'sv': 'swe', 'fa': 'fas', 'ff': 'ful', 'fi': 'fin', 'fj': 'fij',
    'sa': 'san', 'fo': 'fao', 'ka': 'kat', 'kg': 'kon', 'kk': 'kaz',
    'kj': 'kua', 'sq': 'sqi', 'ko': 'kor', 'kn': 'kan', 'km': 'khm',
    'kl': 'kal', 'ks': 'kas', 'kr': 'kau', 'si': 'sin', 'kw': 'cor',
    'kv': 'kom', 'ku': 'kur', 'sl': 'slv', 'sc': 'srd', 'ky': 'kir',
    'sg': 'sag', 'se': 'sme', 'sd': 'snd'
}
ISO639_1 = set([k for k, v in ISO639_1_to_2.items()])

article_types = {
    'ab': 'abstract',
    'an': 'news',
    'ax': 'addendum',
    'co': 'article-commentary',
    'cr': 'case-report',
    'ct': 'research-article',
    'ed': 'editorial',
    'er': 'correction',
    'in': 'editorial',
    'le': 'letter',
    'mt': 'research-article',
    'nd': 'undefined',
    'oa': 'research-article',
    'pr': 'press-release',
    'pv': 'editorial',
    'rc': 'book-review',
    'rn': 'brief-report',
    'ra': 'review-article',
    'sc': 'rapid-communication',
    'tr': 'research-article',
    'up': 'undefined'
}

periodicity = {
    u'M': u'Monthly',
    u'B': u'Bimonthly (every two months)',
    u'Q': u'Quaterly',
    u'T': u'Three times a year',
    u'F': u'Semiannual (twice a year)',
    u'A': u'Annual',
    u'K': u'Irregular (know to be so)',
    u'Z': u'Other frequencies'
}

collections = {
    'scl': ['Brazil', 'www.scielo.br'],
    'arg': ['Argentina', 'www.scielo.org.ar'],
    'cub': ['Cuba', 'scielo.sld.cu'],
    'esp': ['Spain', 'scielo.isciii.es'],
    'col': ['Colombia', 'www.scielo.org.co'],
    'sss': ['Social Sciences', 'socialsciences.scielo.org'],
    'spa': ['Public Health', 'www.scielosp.org'],
    'mex': ['Mexico', 'www.scielo.org.mx'],
    'prt': ['Portugal', 'www.scielo.mec.pt'],
    'cri': ['Costa Rica', 'www.scielo.sa.cr'],
    'ven': ['Venezuela', 'www.scielo.org.ve'],
    'ury': ['Uruguay', 'www.scielo.edu.uy'],
    'per': ['Peru', 'www.scielo.org.pe'],
    'chl': ['Chile', 'www.scielo.cl'],
    'sza': ['South Africa', 'www.scielo.org.za'],
    'bol': ['Bolivia', 'www.scielo.org.bo'],
    'pry': ['Paraguay', 'scielo.iics.una.py'],
    'psi': ['PEPSIC', 'pepsic.bvsalud.org'],
    'ppg': ['PPEGEO', 'ppegeo.igc.usp.br'],
    'rve': ['RevOdonto', 'revodonto.bvsalud.org'],
    'edc': ['Educa', 'educa.fcc.org.br'],
    'inv': [u'Inovação', 'inovacao.scielo.br'],
    'cic': [u'Ciência e Cultura', 'cienciaecultura.bvs.br'],
    'cci': [u'ComCiência', 'comciencia.scielo.br'],
    'wid': ['West Indians', 'caribbean.scielo.org'],
    'pro': ['Proceedings', 'www.proceedings.scielo.br']
}

ISO_3166 = {
    'BD': u'Bangladesh',
    'BE': u'Belgium',
    'BF': u'Burkina Faso',
    'BG': u'Bulgaria',
    'BA': u'Bosnia and Herzegovina',
    'BB': u'Barbados',
    'WF': u'Wallis and Futuna',
    'BL': u'Saint Barthélemy',
    'BM': u'Bermuda',
    'BN': u'Brunei Darussalam',
    'BO': u'Bolivia',
    'BH': u'Bahrain',
    'BI': u'Burundi',
    'BJ': u'Benin',
    'BT': u'Bhutan',
    'BU': u'Burma',
    'BV': u'Bouvet Island',
    'BW': u'Botswana',
    'WS': u'Samoa',
    'BQ': u'British Antarctic Territory',
    'BR': u'Brazil',
    'BS': u'Bahamas',
    'JE': u'Jersey',
    'WK': u'Wake Island',
    'BY': u'Byelorussian SSR',
    'BZ': u'Belize',
    'RU': u'Russian Federation',
    'RW': u'Rwanda',
    'PC': u'Pacific Islands',
    'TL': u'Timor-Leste',
    'JT': u'Johnston Island',
    'TM': u'Turkmenistan',
    'TJ': u'Tajikistan',
    'RO': u'Romania',
    'RH': u'Southern Rhodesia',
    'TK': u'Tokelau',
    'GW': u'Guinea-Bissau',
    'GU': u'Guam',
    'GT': u'Guatemala',
    'GS': u'South Georgia and the South Sandwich Islands',
    'GR': u'Greece',
    'GQ': u'Equatorial Guinea',
    'GP': u'Guadeloupe',
    'JP': u'Japan',
    'GY': u'Guyana',
    'GG': u'Guernsey',
    'GF': u'French Guiana',
    'GE': u'Gilbert and Ellice Islands',
    'GD': u'Grenada',
    'GB': u'United Kingdom',
    'GA': u'Gabon',
    'SV': u'El Salvador',
    'GN': u'Guinea',
    'GM': u'Gambia',
    'GL': u'Greenland',
    'GI': u'Gibraltar',
    'GH': u'Ghana',
    'OM': u'Oman',
    'TN': u'Tunisia',
    'JM': u'Jamaica',
    'JO': u'Jordan',
    'HR': u'Croatia',
    'HV': u'Upper Volta',
    'HT': u'Haiti',
    'HU': u'Hungary',
    'HK': u'Hong Kong',
    'HN': u'Honduras',
    'HM': u'Heard Island and McDonald Islands',
    'VD': u'Viet-Nam',
    'VE': u'Venezuela',
    'PR': u'Puerto Rico',
    'PS': u'Palestine',
    'UA': u'Ukraine',
    'PW': u'Palau',
    'PT': u'Portugal',
    'PU': u'United States Miscellaneous Pacific Islands',
    'PZ': u'Panama Canal Zone',
    'PY': u'Paraguay',
    'IQ': u'Iraq',
    'PA': u'Panama',
    'PF': u'French Polynesia',
    'PG': u'Papua New Guinea',
    'PE': u'Peru',
    'PK': u'Pakistan',
    'PH': u'Philippines',
    'PN': u'Pitcairn',
    'PL': u'Poland',
    'PM': u'Saint Pierre and Miquelon',
    'ZM': u'Zambia',
    'EH': u'Western Sahara',
    'EE': u'Estonia',
    'EG': u'Egypt',
    'ZA': u'South Africa',
    'EC': u'Ecuador',
    'IT': u'Italy',
    'VN': u'Viet Nam',
    'SB': u'Solomon Islands',
    'ET': u'Ethiopia',
    'SO': u'Somalia',
    'ZW': u'Zimbabwe',
    'SA': u'Saudi Arabia',
    'ES': u'Spain',
    'ER': u'Eritrea',
    'ME': u'Montenegro',
    'MD': u'Moldova',
    'MG': u'Madagascar',
    'MF': u'Saint Martin',
    'MA': u'Morocco',
    'MC': u'Monaco',
    'UZ': u'Uzbekistan',
    'MM': u'Myanmar',
    'ML': u'Mali',
    'MO': u'Macao',
    'MN': u'Mongolia',
    'MI': u'Midway Islands',
    'MH': u'Marshall Islands',
    'MK': u'Macedonia',
    'MU': u'Mauritius',
    'MT': u'Malta',
    'MW': u'Malawi',
    'MV': u'Maldives',
    'MQ': u'Martinique',
    'MP': u'Northern Mariana Islands',
    'MS': u'Montserrat',
    'MR': u'Mauritania',
    'IM': u'Isle of Man',
    'UG': u'Uganda',
    'TZ': u'Tanzania',
    'MY': u'Malaysia',
    'MX': u'Mexico',
    'IL': u'Israel',
    'FQ': u'French Southern and Antarctic Territories',
    'FR': u'France',
    'IO': u'British Indian Ocean Territory',
    'SH': u'Saint Helena',
    'RE': u'Réunion',
    'SJ': u'Svalbard and Jan Mayen',
    'FI': u'Finland',
    'FJ': u'Fiji',
    'FK': u'Falkland Islands',
    'FM': u'Micronesia',
    'FO': u'Faroe Islands',
    'NH': u'New Hebrides',
    'NI': u'Nicaragua',
    'NL': u'Netherlands',
    'NO': u'Norway',
    'NA': u'Namibia',
    'VU': u'Vanuatu',
    'NC': u'New Caledonia',
    'NE': u'Niger',
    'NF': u'Norfolk Island',
    'NG': u'Nigeria',
    'NZ': u'New Zealand',
    'ZR': u'Zaire',
    'NP': u'Nepal',
    'NQ': u'Dronning Maud Land',
    'NR': u'Nauru',
    'NT': u'Neutral Zone',
    'NU': u'Niue',
    'CK': u'Cook Islands',
    'CI': u"Côte d'Ivoire",
    'CH': u'Switzerland',
    'CO': u'Colombia',
    'CN': u'China',
    'CM': u'Cameroon',
    'CL': u'Chile',
    'CC': u'Cocos',
    'CA': u'Canada',
    'CG': u'Congo',
    'CF': u'Central African Republic',
    'CD': u'Congo',
    'CZ': u'Czech Republic',
    'CY': u'Cyprus',
    'CX': u'Christmas Island',
    'CS': u'Czechoslovakia',
    'CR': u'Costa Rica',
    'CW': u'Curaçao',
    'CV': u'Cabo Verde',
    'CU': u'Cuba',
    'CT': u'Canton and Enderbury Islands',
    'SZ': u'Swaziland',
    'SY': u'Syrian Arab Republic',
    'SX': u'Sint Maarten',
    'KG': u'Kyrgyzstan',
    'KE': u'Kenya',
    'SS': u'South Sudan',
    'SR': u'Suriname',
    'KI': u'Kiribati',
    'KH': u'Cambodia',
    'KN': u'Saint Kitts and Nevis',
    'KM': u'Comoros',
    'ST': u'Sao Tome and Principe',
    'SK': u'Slovakia',
    'KR': u'Korea',
    'SI': u'Slovenia',
    'KP': u'Korea',
    'KW': u'Kuwait',
    'SN': u'Senegal',
    'SM': u'San Marino',
    'SL': u'Sierra Leone',
    'SC': u'Seychelles',
    'KZ': u'Kazakhstan',
    'KY': u'Cayman Islands',
    'SG': u'Singapore',
    'SE': u'Sweden',
    'SD': u'Sudan',
    'DO': u'Dominican Republic',
    'DM': u'Dominica',
    'DJ': u'Djibouti',
    'DK': u'Denmark',
    'VG': u'Virgin Islands',
    'DD': u'German Democratic Republic',
    'DE': u'Germany',
    'YE': u'Yemen',
    'YD': u'Yemen',
    'DZ': u'Algeria',
    'US': u'United States',
    'DY': u'Dahomey',
    'UY': u'Uruguay',
    'YU': u'Yugoslavia',
    'YT': u'Mayotte',
    'UM': u'United States Minor Outlying Islands',
    'LB': u'Lebanon',
    'LC': u'Saint Lucia',
    'LA': u"Lao People's Democratic Republic",
    'TV': u'Tuvalu',
    'TW': u'Taiwan',
    'TT': u'Trinidad and Tobago',
    'TR': u'Turkey',
    'LK': u'Sri Lanka',
    'TP': u'East Timor',
    'LI': u'Liechtenstein',
    'LV': u'Latvia',
    'TO': u'Tonga',
    'LT': u'Lithuania',
    'LU': u'Luxembourg',
    'LR': u'Liberia',
    'LS': u'Lesotho',
    'TH': u'Thailand',
    'TF': u'French Southern Territories',
    'TG': u'Togo',
    'TD': u'Chad',
    'TC': u'Turks and Caicos Islands',
    'LY': u'Libya',
    'VA': u'Holy See',
    'VC': u'Saint Vincent and the Grenadines',
    'AE': u'United Arab Emirates',
    'AD': u'Andorra',
    'AG': u'Antigua and Barbuda',
    'AF': u'Afghanistan',
    'AI': u'Anguilla',
    'VI': u'Virgin Islands',
    'IS': u'Iceland',
    'IR': u'Iran',
    'AM': u'Armenia',
    'AL': u'Albania',
    'AO': u'Angola',
    'AN': u'Netherlands Antilles',
    'AQ': u'Antarctica',
    'AS': u'American Samoa',
    'AR': u'Argentina',
    'AU': u'Australia',
    'AT': u'Austria',
    'AW': u'Aruba',
    'IN': u'India',
    'AX': u'Âland Islands',
    'AZ': u'Azerbaijan',
    'IE': u'Ireland',
    'ID': u'Indonesia',
    'RS': u'Serbia',
    'QA': u'Qatar',
    'MZ': u'Mozambique'
}

journal_status = {
    'c': 'current',
    'd': 'deceased',
    '?': 'inprogress',
    'p': 'inprogress',
    's': 'suspended'
}



















