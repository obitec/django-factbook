# IMPORTS
# ---------------------------------------------------------------------------------------------------------------------#
from logging import getLogger

import requests
from django.core.management.base import BaseCommand

from modules.fact_book.models import Country, Currency, Continent, Region

# IMPORTS
# ---------------------------------------------------------------------------------------------------------------------#
logger = getLogger('django')


# GLOBALS
# ---------------------------------------------------------------------------------------------------------------------#
COUNTRIES = {
    'AT': {'position': 1, 'display_name': "Austria"},
    'BE': {'position': 2, 'display_name': "Belgium"},
    'BG': {'position': 3, 'display_name': "Bulgaria"},
    'HR': {'position': 4, 'display_name': "Croatia"},
    'CY': {'position': 5, 'display_name': "Cyprus"},
    'CZ': {'position': 6, 'display_name': "Czech Republic"},
    'DK': {'position': 7, 'display_name': "Denmark"},
    'EE': {'position': 8, 'display_name': "Estonia"},
    'FI': {'position': 9, 'display_name': "Finland"},
    'FR': {'position': 10, 'display_name': "France"},
    'DE': {'position': 11, 'display_name': "Germany"},
    'GR': {'position': 12, 'display_name': "Greece"},
    'HU': {'position': 13, 'display_name': "Hungary"},
    'IE': {'position': 14, 'display_name': "Ireland"},
    'IT': {'position': 15, 'display_name': "Italy"},
    'LV': {'position': 16, 'display_name': "Latvia"},
    'LT': {'position': 17, 'display_name': "Lithuania"},
    'LU': {'position': 18, 'display_name': "Luxembourg"},
    'MT': {'position': 19, 'display_name': "Malta"},
    'NL': {'position': 20, 'display_name': "Netherlands"},
    'PL': {'position': 21, 'display_name': "Poland"},
    'PT': {'position': 22, 'display_name': "Portugal"},
    'RO': {'position': 23, 'display_name': "Romania"},
    'SK': {'position': 24, 'display_name': "Slovakia"},
    'SI': {'position': 25, 'display_name': "Slovenia"},
    'ES': {'position': 26, 'display_name': "Spain"},
    'SE': {'position': 27, 'display_name': "Sweden"},
    'GB': {'position': 28, 'display_name': "United Kingdom"},
    'AF': {'position': 29, 'display_name': "Afghanistan"},
    'AX': {'position': 30, 'display_name': "Åland Islands"},
    'AL': {'position': 31, 'display_name': "Albania"},
    'DZ': {'position': 32, 'display_name': "Algeria"},
    'AS': {'position': 33, 'display_name': "American Samoa"},
    'AD': {'position': 34, 'display_name': "Andorra"},
    'AO': {'position': 35, 'display_name': "Angola"},
    'AI': {'position': 36, 'display_name': "Anguilla"},
    'AQ': {'position': 37, 'display_name': "Antarctica"},
    'AG': {'position': 38, 'display_name': "Antigua and Barbuda"},
    'AR': {'position': 39, 'display_name': "Argentina"},
    'AM': {'position': 40, 'display_name': "Armenia"},
    'AW': {'position': 41, 'display_name': "Aruba"},
    'AU': {'position': 42, 'display_name': "Australia"},
    'AZ': {'position': 43, 'display_name': "Azerbaijan"},
    'BS': {'position': 44, 'display_name': "Bahamas"},
    'BH': {'position': 45, 'display_name': "Bahrain"},
    'BD': {'position': 46, 'display_name': "Bangladesh"},
    'BB': {'position': 47, 'display_name': "Barbados"},
    'BY': {'position': 48, 'display_name': "Belarus"},
    'BZ': {'position': 49, 'display_name': "Belize"},
    'BJ': {'position': 50, 'display_name': "Benin"},
    'BM': {'position': 51, 'display_name': "Bermuda"},
    'BT': {'position': 52, 'display_name': "Bhutan"},
    'BO': {'position': 53, 'display_name': "Bolivia"},
    'BQ': {'position': 54, 'display_name': "Bonaire, Sint Eustatius and Saba"},
    'BA': {'position': 55, 'display_name': "Bosnia and Herzegovina"},
    'BW': {'position': 56, 'display_name': "Botswana"},
    'BV': {'position': 57, 'display_name': "Bouvet Island"},
    'BR': {'position': 58, 'display_name': "Brazil"},
    'IO': {'position': 59, 'display_name': "British Indian Ocean Territory"},
    'BN': {'position': 60, 'display_name': "Brunei Darussalam"},
    'BF': {'position': 61, 'display_name': "Burkina Faso"},
    'BI': {'position': 62, 'display_name': "Burundi"},
    'CV': {'position': 63, 'display_name': "Cape Verde"},
    'KH': {'position': 64, 'display_name': "Cambodia"},
    'CM': {'position': 65, 'display_name': "Cameroon"},
    'CA': {'position': 66, 'display_name': "Canada"},
    'KY': {'position': 67, 'display_name': "Cayman Islands"},
    'CF': {'position': 68, 'display_name': "Central African Republic"},
    'TD': {'position': 69, 'display_name': "Chad"},
    'CL': {'position': 70, 'display_name': "Chile"},
    'CN': {'position': 71, 'display_name': "China"},
    'CX': {'position': 72, 'display_name': "Christmas Island"},
    'CC': {'position': 73, 'display_name': "Cocos (Keeling) Islands"},
    'CO': {'position': 74, 'display_name': "Colombia"},
    'KM': {'position': 75, 'display_name': "Comoros"},
    'CG': {'position': 76, 'display_name': "Congo"},
    'CD': {'position': 77, 'display_name': "Congo, the Democratic Republic of the"},
    'CK': {'position': 78, 'display_name': "Cook Islands"},
    'CR': {'position': 79, 'display_name': "Costa Rica"},
    'CI': {'position': 80, 'display_name': "Ivory Coast"},
    'CU': {'position': 81, 'display_name': "Cuba"},
    'CW': {'position': 82, 'display_name': "Curaçao"},
    'DJ': {'position': 83, 'display_name': "Djibouti"},
    'DM': {'position': 84, 'display_name': "Dominica"},
    'DO': {'position': 85, 'display_name': "Dominican Republic"},
    'EC': {'position': 86, 'display_name': "Ecuador"},
    'EG': {'position': 87, 'display_name': "Egypt"},
    'SV': {'position': 88, 'display_name': "El Salvador"},
    'GQ': {'position': 89, 'display_name': "Equatorial Guinea"},
    'ER': {'position': 90, 'display_name': "Eritrea"},
    'ET': {'position': 91, 'display_name': "Ethiopia"},
    'FK': {'position': 92, 'display_name': "Falkland Islands (Malvinas)"},
    'FO': {'position': 93, 'display_name': "Faroe Islands"},
    'FJ': {'position': 94, 'display_name': "Fiji"},
    'GF': {'position': 95, 'display_name': "French Guiana"},
    'PF': {'position': 96, 'display_name': "French Polynesia"},
    'TF': {'position': 97, 'display_name': "French Southern Territories"},
    'GA': {'position': 98, 'display_name': "Gabon"},
    'GM': {'position': 99, 'display_name': "Gambia"},
    'GE': {'position': 100, 'display_name': "Georgia"},
    'GH': {'position': 101, 'display_name': "Ghana"},
    'GI': {'position': 102, 'display_name': "Gibraltar"},
    'GL': {'position': 103, 'display_name': "Greenland"},
    'GD': {'position': 104, 'display_name': "Grenada"},
    'GP': {'position': 105, 'display_name': "Guadeloupe"},
    'GU': {'position': 106, 'display_name': "Guam"},
    'GT': {'position': 107, 'display_name': "Guatemala"},
    'GG': {'position': 108, 'display_name': "Guernsey"},
    'GN': {'position': 109, 'display_name': "Guinea"},
    'GW': {'position': 110, 'display_name': "Guinea-Bissau"},
    'GY': {'position': 111, 'display_name': "Guyana"},
    'HT': {'position': 112, 'display_name': "Haiti"},
    'HM': {'position': 113, 'display_name': "Heard Island and McDonald Islands"},
    'VA': {'position': 114, 'display_name': "Holy See (Vatican City State)"},
    'HN': {'position': 115, 'display_name': "Honduras"},
    'HK': {'position': 116, 'display_name': "Hong Kong"},
    'IS': {'position': 117, 'display_name': "Iceland"},
    'IN': {'position': 118, 'display_name': "India"},
    'ID': {'position': 119, 'display_name': "Indonesia"},
    'IR': {'position': 120, 'display_name': "Iran"},
    'IQ': {'position': 121, 'display_name': "Iraq"},
    'IM': {'position': 122, 'display_name': "Isle of Man"},
    'IL': {'position': 123, 'display_name': "Israel"},
    'JM': {'position': 124, 'display_name': "Jamaica"},
    'JP': {'position': 125, 'display_name': "Japan"},
    'JE': {'position': 126, 'display_name': "Jersey"},
    'JO': {'position': 127, 'display_name': "Jordan"},
    'KZ': {'position': 128, 'display_name': "Kazakhstan"},
    'KE': {'position': 129, 'display_name': "Kenya"},
    'KI': {'position': 130, 'display_name': "Kiribati"},
    'KP': {'position': 131, 'display_name': "Korea, Democratic People's Republic of"},
    'KR': {'position': 132, 'display_name': "Korea, Republic of"},
    'KW': {'position': 133, 'display_name': "Kuwait"},
    'KG': {'position': 134, 'display_name': "Kyrgyzstan"},
    'LA': {'position': 135, 'display_name': "Lao People's Democratic Republic"},
    'LB': {'position': 136, 'display_name': "Lebanon"},
    'LS': {'position': 137, 'display_name': "Lesotho"},
    'LR': {'position': 138, 'display_name': "Liberia"},
    'LY': {'position': 139, 'display_name': "Libya"},
    'LI': {'position': 140, 'display_name': "Liechtenstein"},
    'MO': {'position': 141, 'display_name': "Macao"},
    'MK': {'position': 142, 'display_name': "Macedonia"},
    'MG': {'position': 143, 'display_name': "Madagascar"},
    'MW': {'position': 144, 'display_name': "Malawi"},
    'MY': {'position': 145, 'display_name': "Malaysia"},
    'MV': {'position': 146, 'display_name': "Maldives"},
    'ML': {'position': 147, 'display_name': "Mali"},
    'MH': {'position': 148, 'display_name': "Marshall Islands"},
    'MQ': {'position': 149, 'display_name': "Martinique"},
    'MR': {'position': 150, 'display_name': "Mauritania"},
    'MU': {'position': 151, 'display_name': "Mauritius"},
    'YT': {'position': 152, 'display_name': "Mayotte"},
    'MX': {'position': 153, 'display_name': "Mexico"},
    'FM': {'position': 154, 'display_name': "Micronesia, Federated States of"},
    'MD': {'position': 155, 'display_name': "Moldova, Republic of"},
    'MC': {'position': 156, 'display_name': "Monaco"},
    'MN': {'position': 157, 'display_name': "Mongolia"},
    'ME': {'position': 158, 'display_name': "Montenegro"},
    'MS': {'position': 159, 'display_name': "Montserrat"},
    'MA': {'position': 160, 'display_name': "Morocco"},
    'MZ': {'position': 161, 'display_name': "Mozambique"},
    'MM': {'position': 162, 'display_name': "Myanmar"},
    'NA': {'position': 163, 'display_name': "Namibia"},
    'NR': {'position': 164, 'display_name': "Nauru"},
    'NP': {'position': 165, 'display_name': "Nepal"},
    'NC': {'position': 166, 'display_name': "New Caledonia"},
    'NZ': {'position': 167, 'display_name': "New Zealand"},
    'NI': {'position': 168, 'display_name': "Nicaragua"},
    'NE': {'position': 169, 'display_name': "Niger"},
    'NG': {'position': 170, 'display_name': "Nigeria"},
    'NU': {'position': 171, 'display_name': "Niue"},
    'NF': {'position': 172, 'display_name': "Norfolk Island"},
    'MP': {'position': 173, 'display_name': "Northern Mariana Islands"},
    'NO': {'position': 174, 'display_name': "Norway"},
    'OM': {'position': 175, 'display_name': "Oman"},
    'PK': {'position': 176, 'display_name': "Pakistan"},
    'PW': {'position': 177, 'display_name': "Palau"},
    'PS': {'position': 178, 'display_name': "Palestine, State of"},
    'PA': {'position': 179, 'display_name': "Panama"},
    'PG': {'position': 180, 'display_name': "Papua New Guinea"},
    'PY': {'position': 181, 'display_name': "Paraguay"},
    'PE': {'position': 182, 'display_name': "Peru"},
    'PH': {'position': 183, 'display_name': "Philippines"},
    'PN': {'position': 184, 'display_name': "Pitcairn"},
    'PR': {'position': 185, 'display_name': "Puerto Rico"},
    'QA': {'position': 186, 'display_name': "Qatar"},
    'RE': {'position': 187, 'display_name': "Réunion"},
    'RU': {'position': 188, 'display_name': "Russian Federation"},
    'RW': {'position': 189, 'display_name': "Rwanda"},
    'BL': {'position': 190, 'display_name': "Saint Barthélemy"},
    'SH': {'position': 191, 'display_name': "Saint Helena, Ascension and Tristan da Cunha"},
    'KN': {'position': 192, 'display_name': "Saint Kitts and Nevis"},
    'LC': {'position': 193, 'display_name': "Saint Lucia"},
    'MF': {'position': 194, 'display_name': "Saint Martin (French part)"},
    'PM': {'position': 195, 'display_name': "Saint Pierre and Miquelon"},
    'VC': {'position': 196, 'display_name': "Saint Vincent and the Grenadines"},
    'WS': {'position': 197, 'display_name': "Samoa"},
    'SM': {'position': 198, 'display_name': "San Marino"},
    'ST': {'position': 199, 'display_name': "Sao Tome and Principe"},
    'SA': {'position': 200, 'display_name': "Saudi Arabia"},
    'SN': {'position': 201, 'display_name': "Senegal"},
    'RS': {'position': 202, 'display_name': "Serbia"},
    'SC': {'position': 203, 'display_name': "Seychelles"},
    'SL': {'position': 204, 'display_name': "Sierra Leone"},
    'SG': {'position': 205, 'display_name': "Singapore"},
    'SX': {'position': 206, 'display_name': "Sint Maarten (Dutch part)"},
    'SB': {'position': 207, 'display_name': "Solomon Islands"},
    'SO': {'position': 208, 'display_name': "Somalia"},
    'ZA': {'position': 209, 'display_name': "South Africa"},
    'GS': {'position': 210, 'display_name': "South Georgia and the South Sandwich Islands"},
    'SS': {'position': 211, 'display_name': "South Sudan"},
    'LK': {'position': 212, 'display_name': "Sri Lanka"},
    'SD': {'position': 213, 'display_name': "Sudan"},
    'SR': {'position': 214, 'display_name': "Suriname"},
    'SJ': {'position': 215, 'display_name': "Svalbard and Jan Mayen"},
    'SZ': {'position': 216, 'display_name': "Swaziland"},
    'CH': {'position': 217, 'display_name': "Switzerland"},
    'SY': {'position': 218, 'display_name': "Syrian Arab Republic"},
    'TW': {'position': 219, 'display_name': "Taiwan, Province of China"},
    'TJ': {'position': 220, 'display_name': "Tajikistan"},
    'TZ': {'position': 221, 'display_name': "Tanzania, United Republic of"},
    'TH': {'position': 222, 'display_name': "Thailand"},
    'TL': {'position': 223, 'display_name': "Timor-Leste"},
    'TG': {'position': 224, 'display_name': "Togo"},
    'TK': {'position': 225, 'display_name': "Tokelau"},
    'TO': {'position': 226, 'display_name': "Tonga"},
    'TT': {'position': 227, 'display_name': "Trinidad and Tobago"},
    'TN': {'position': 228, 'display_name': "Tunisia"},
    'TR': {'position': 229, 'display_name': "Turkey"},
    'TM': {'position': 230, 'display_name': "Turkmenistan"},
    'TC': {'position': 231, 'display_name': "Turks and Caicos Islands"},
    'TV': {'position': 232, 'display_name': "Tuvalu"},
    'UG': {'position': 233, 'display_name': "Uganda"},
    'UA': {'position': 234, 'display_name': "Ukraine"},
    'AE': {'position': 235, 'display_name': "United Arab Emirates"},
    'US': {'position': 236, 'display_name': "United States"},
    'UM': {'position': 237, 'display_name': "United States Minor Outlying Islands"},
    'UY': {'position': 238, 'display_name': "Uruguay"},
    'UZ': {'position': 239, 'display_name': "Uzbekistan"},
    'VU': {'position': 240, 'display_name': "Vanuatu"},
    'VE': {'position': 241, 'display_name': "Venezuela, Bolivarian Republic of"},
    'VN': {'position': 242, 'display_name': "Vietnam"},
    'VG': {'position': 243, 'display_name': "Virgin Islands, British"},
    'VI': {'position': 244, 'display_name': "Virgin Islands, U.S."},
    'WF': {'position': 245, 'display_name': "Wallis and Futuna"},
    'EH': {'position': 246, 'display_name': "Western Sahara"},
    'YE': {'position': 247, 'display_name': "Yemen"},
    'ZM': {'position': 248, 'display_name': "Zambia"},
    'ZW': {'position': 249, 'display_name': "Zimbabwe"},
    'XK': {'position': 250, 'display_name': "Republic of Kosovo"},
}

CURRENCIES = {
    'AED': {
        'symbol': '',
        'name': 'United Arab Emirates Dirham',
        'url': 'http://xe.com/currency/?currency=aed-emirati-dirham'},
    'AFN': {
        'symbol': '؋',
        'name': 'Afghanistan Afghani',
        'url': 'http://xe.com/currency/?currency=afn-afghan-afghani'},
    'ALL': {
        'symbol': 'Lek',
        'name': 'Albania Lek',
        'url': 'http://xe.com/currency/?currency=all-albanian-lek'},
    'AMD': {
        'symbol': '',
        'name': 'Armenia Dram',
        'url': 'http://xe.com/currency/?currency=amd-armenian-dram'},
    'ANG': {
        'symbol': 'ƒ',
        'name': 'Netherlands Antilles Guilder',
        'url': 'http://xe.com/currency/?currency=ang-dutch-guilder'},
    'AOA': {
        'symbol': '',
        'name': 'Angola Kwanza',
        'url': 'http://xe.com/currency/?currency=aoa-angolan-kwanza'},
    'ARS': {
        'symbol': '$',
        'name': 'Argentina Peso',
        'url': 'http://xe.com/currency/?currency=ars-argentine-peso'},
    'AUD': {
        'symbol': '$',
        'name': 'Australia Dollar',
        'url': 'http://xe.com/currency/?currency=aud-australian-dollar'},
    'AWG': {
        'symbol': 'ƒ',
        'name': 'Aruba Guilder',
        'url': 'http://xe.com/currency/?currency=awg-aruban-or-dutch-guilder'},
    'AZN': {
        'symbol': 'ман',
        'name': 'Azerbaijan New Manat',
        'url': 'http://xe.com/currency/?currency=azn-azerbaijani-new-manat'},
    'BAM': {
        'symbol': 'KM',
        'name': 'Bosnia and Herzegovina Convertible Marka',
        'url': 'http://xe.com/currency/?currency=bam-bosnian-convertible-marka'},
    'BBD': {
        'symbol': '$',
        'name': 'Barbados Dollar',
        'url': 'http://xe.com/currency/?currency=bbd-barbadian-or-bajan-dollar'},
    'BDT': {
        'symbol': '',
        'name': 'Bangladesh Taka',
        'url': 'http://xe.com/currency/?currency=bdt-bangladeshi-taka'},
    'BGN': {
        'symbol': 'лв',
        'name': 'Bulgaria Lev',
        'url': 'http://xe.com/currency/?currency=bgn-bulgarian-lev'},
    'BHD': {
        'symbol': '',
        'name': 'Bahrain Dinar',
        'url': 'http://xe.com/currency/?currency=bhd-bahraini-dinar'},
    'BIF': {
        'symbol': '',
        'name': 'Burundi Franc',
        'url': 'http://xe.com/currency/?currency=bif-burundian-franc'},
    'BMD': {
        'symbol': '$',
        'name': 'Bermuda Dollar',
        'url': 'http://xe.com/currency/?currency=bmd-bermudian-dollar'},
    'BND': {
        'symbol': '$',
        'name': 'Brunei Darussalam Dollar',
        'url': 'http://xe.com/currency/?currency=bnd-bruneian-dollar'},
    'BOB': {
        'symbol': '$b',
        'name': 'Bolivia Boliviano',
        'url': 'http://xe.com/currency/?currency=bob-bolivian-boliviano'},
    'BRL': {
        'symbol': 'R$',
        'name': 'Brazil Real',
        'url': 'http://xe.com/currency/?currency=brl-brazilian-real'},
    'BSD': {
        'symbol': '$',
        'name': 'Bahamas Dollar',
        'url': 'http://xe.com/currency/?currency=bsd-bahamian-dollar'},
    'BTN': {
        'symbol': '',
        'name': 'Bhutan Ngultrum',
        'url': 'http://xe.com/currency/?currency=btn-bhutanese-ngultrum'},
    'BWP': {
        'symbol': 'P',
        'name': 'Botswana Pula',
        'url': 'http://xe.com/currency/?currency=bwp-botswana-pula'},
    'BYR': {
        'symbol': 'p.',
        'name': 'Belarus Ruble',
        'url': 'http://xe.com/currency/?currency=byr-belarusian-ruble'},
    'BZD': {
        'symbol': 'BZ$',
        'name': 'Belize Dollar',
        'url': 'http://xe.com/currency/?currency=bzd-belizean-dollar'},
    'CAD': {
        'symbol': '$',
        'name': 'Canada Dollar',
        'url': 'http://xe.com/currency/?currency=cad-canadian-dollar'},
    'CDF': {
        'symbol': '',
        'name': 'Congo/Kinshasa Franc',
        'url': 'http://xe.com/currency/?currency=cdf-congolese-franc'},
    'CHF': {
        'symbol': 'CHF',
        'name': 'Switzerland Franc',
        'url': 'http://xe.com/currency/?currency=chf-swiss-franc'},
    'CLP': {
        'symbol': '$',
        'name': 'Chile Peso',
        'url': 'http://xe.com/currency/?currency=clp-chilean-peso'},
    'CNY': {
        'symbol': '¥',
        'name': 'China Yuan Renminbi',
        'url': 'http://xe.com/currency/?currency=cny-chinese-yuan-renminbi'},
    'COP': {
        'symbol': '$',
        'name': 'Colombia Peso',
        'url': 'http://xe.com/currency/?currency=cop-colombian-peso'},
    'CRC': {
        'symbol': '₡',
        'name': 'Costa Rica Colon',
        'url': 'http://xe.com/currency/?currency=crc-costa-rican-colon'},
    'CUC': {
        'symbol': '',
        'name': 'Cuba Convertible Peso',
        'url': 'http://xe.com/currency/?currency=cuc-cuban-convertible-peso'},
    'CUP': {
        'symbol': '₱',
        'name': 'Cuba Peso',
        'url': 'http://xe.com/currency/?currency=cup-cuban-peso'},
    'CVE': {
        'symbol': '',
        'name': 'Cape Verde Escudo',
        'url': 'http://xe.com/currency/?currency=cve-cape-verdean-escudo'},
    'CZK': {
        'symbol': 'Kč',
        'name': 'Czech Republic Koruna',
        'url': 'http://xe.com/currency/?currency=czk-czech-koruna'},
    'DJF': {
        'symbol': '',
        'name': 'Djibouti Franc',
        'url': 'http://xe.com/currency/?currency=djf-djiboutian-franc'},
    'DKK': {
        'symbol': 'kr',
        'name': 'Denmark Krone',
        'url': 'http://xe.com/currency/?currency=dkk-danish-krone'},
    'DOP': {
        'symbol': 'RD$',
        'name': 'Dominican Republic Peso',
        'url': 'http://xe.com/currency/?currency=dop-dominican-peso'},
    'DZD': {
        'symbol': '',
        'name': 'Algeria Dinar',
        'url': 'http://xe.com/currency/?currency=dzd-algerian-dinar'},
    'EGP': {
        'symbol': '£',
        'name': 'Egypt Pound',
        'url': 'http://xe.com/currency/?currency=egp-egyptian-pound'},
    'ERN': {
        'symbol': '',
        'name': 'Eritrea Nakfa',
        'url': 'http://xe.com/currency/?currency=ern-eritrean-nakfa'},
    'ETB': {
        'symbol': '',
        'name': 'Ethiopia Birr',
        'url': 'http://xe.com/currency/?currency=etb-ethiopian-birr'},
    'EUR': {
        'symbol': '€',
        'name': 'Euro Member Countries',
        'url': 'http://xe.com/currency/?currency=eur-euro'},
    'FJD': {
        'symbol': '$',
        'name': 'Fiji Dollar',
        'url': 'http://xe.com/currency/?currency=fjd-fijian-dollar'},
    'FKP': {
        'symbol': '£',
        'name': 'Falkland Islands (Malvinas) Pound',
        'url': 'http://xe.com/currency/?currency=fkp-falkland-island-pound'},
    'GBP': {
        'symbol': '£',
        'name': 'United Kingdom Pound',
        'url': 'http://xe.com/currency/?currency=gbp-british-pound'},
    'GEL': {
        'symbol': '',
        'name': 'Georgia Lari',
        'url': 'http://xe.com/currency/?currency=gel-georgian-lari'},
    'GGP': {
        'symbol': '£',
        'name': 'Guernsey Pound',
        'url': 'http://xe.com/currency/?currency=ggp-guernsey-pound'},
    'GHS': {
        'symbol': '¢',
        'name': 'Ghana Cedi',
        'url': 'http://xe.com/currency/?currency=ghs-ghanaian-cedi'},
    'GIP': {
        'symbol': '£',
        'name': 'Gibraltar Pound',
        'url': 'http://xe.com/currency/?currency=gip-gibraltar-pound'},
    'GMD': {
        'symbol': '',
        'name': 'Gambia Dalasi',
        'url': 'http://xe.com/currency/?currency=gmd-gambian-dalasi'},
    'GNF': {
        'symbol': '',
        'name': 'Guinea Franc',
        'url': 'http://xe.com/currency/?currency=gnf-guinean-franc'},
    'GTQ': {
        'symbol': 'Q',
        'name': 'Guatemala Quetzal',
        'url': 'http://xe.com/currency/?currency=gtq-guatemalan-quetzal'},
    'GYD': {
        'symbol': '$',
        'name': 'Guyana Dollar',
        'url': 'http://xe.com/currency/?currency=gyd-guyanese-dollar'},
    'HKD': {
        'symbol': '$',
        'name': 'Hong Kong Dollar',
        'url': 'http://xe.com/currency/?currency=hkd-hong-kong-dollar'},
    'HNL': {
        'symbol': 'L',
        'name': 'Honduras Lempira',
        'url': 'http://xe.com/currency/?currency=hnl-honduran-lempira'},
    'HRK': {
        'symbol': 'kn',
        'name': 'Croatia Kuna',
        'url': 'http://xe.com/currency/?currency=hrk-croatian-kuna'},
    'HTG': {
        'symbol': '',
        'name': 'Haiti Gourde',
        'url': 'http://xe.com/currency/?currency=htg-haitian-gourde'},
    'HUF': {
        'symbol': 'Ft',
        'name': 'Hungary Forint',
        'url': 'http://xe.com/currency/?currency=huf-hungarian-forint'},
    'IDR': {
        'symbol': 'Rp',
        'name': 'Indonesia Rupiah',
        'url': 'http://xe.com/currency/?currency=idr-indonesian-rupiah'},
    'ILS': {
        'symbol': '₪',
        'name': 'Israel Shekel',
        'url': 'http://xe.com/currency/?currency=ils-israeli-shekel'},
    'IMP': {
        'symbol': '£',
        'name': 'Isle of Man Pound',
        'url': 'http://xe.com/currency/?currency=imp-isle-of-man-pound'},
    'INR': {
        'symbol': '₹',
        'name': 'India Rupee',
        'url': 'http://xe.com/currency/?currency=inr-indian-rupee'},
    'IQD': {
        'symbol': '',
        'name': 'Iraq Dinar',
        'url': 'http://xe.com/currency/?currency=iqd-iraqi-dinar'},
    'IRR': {
        'symbol': '﷼',
        'name': 'Iran Rial',
        'url': 'http://xe.com/currency/?currency=irr-iranian-rial'},
    'ISK': {
        'symbol': 'kr',
        'name': 'Iceland Krona',
        'url': 'http://xe.com/currency/?currency=isk-icelandic-krona'},
    'JEP': {
        'symbol': '£',
        'name': 'Jersey Pound',
        'url': 'http://xe.com/currency/?currency=jep-jersey-pound'},
    'JMD': {
        'symbol': 'J$',
        'name': 'Jamaica Dollar',
        'url': 'http://xe.com/currency/?currency=jmd-jamaican-dollar'},
    'JOD': {
        'symbol': '',
        'name': 'Jordan Dinar',
        'url': 'http://xe.com/currency/?currency=jod-jordanian-dinar'},
    'JPY': {
        'symbol': '¥',
        'name': 'Japan Yen',
        'url': 'http://xe.com/currency/?currency=jpy-japanese-yen'},
    'KES': {
        'symbol': '',
        'name': 'Kenya Shilling',
        'url': 'http://xe.com/currency/?currency=kes-kenyan-shilling'},
    'KGS': {
        'symbol': 'лв',
        'name': 'Kyrgyzstan Som',
        'url': 'http://xe.com/currency/?currency=kgs-kyrgyzstani-som'},
    'KHR': {
        'symbol': '៛',
        'name': 'Cambodia Riel',
        'url': 'http://xe.com/currency/?currency=khr-cambodian-riel'},
    'KMF': {
        'symbol': '',
        'name': 'Comoros Franc',
        'url': 'http://xe.com/currency/?currency=kmf-comoran-franc'},
    'KPW': {
        'symbol': '₩',
        'name': 'Korea (North) Won',
        'url': 'http://xe.com/currency/?currency=kpw-north-korean-won'},
    'KRW': {
        'symbol': '₩',
        'name': 'Korea (South) Won',
        'url': 'http://xe.com/currency/?currency=krw-south-korean-won'},
    'KWD': {
        'symbol': '',
        'name': 'Kuwait Dinar',
        'url': 'http://xe.com/currency/?currency=kwd-kuwaiti-dinar'},
    'KYD': {
        'symbol': '$',
        'name': 'Cayman Islands Dollar',
        'url': 'http://xe.com/currency/?currency=kyd-caymanian-dollar'},
    'KZT': {
        'symbol': 'лв',
        'name': 'Kazakhstan Tenge',
        'url': 'http://xe.com/currency/?currency=kzt-kazakhstani-tenge'},
    'LAK': {
        'symbol': '₭',
        'name': 'Laos Kip',
        'url': 'http://xe.com/currency/?currency=lak-lao-or-laotian-kip'},
    'LBP': {
        'symbol': '£',
        'name': 'Lebanon Pound',
        'url': 'http://xe.com/currency/?currency=lbp-lebanese-pound'},
    'LKR': {
        'symbol': '₨',
        'name': 'Sri Lanka Rupee',
        'url': 'http://xe.com/currency/?currency=lkr-sri-lankan-rupee'},
    'LRD': {
        'symbol': '$',
        'name': 'Liberia Dollar',
        'url': 'http://xe.com/currency/?currency=lrd-liberian-dollar'},
    'LSL': {
        'symbol': '',
        'name': 'Lesotho Loti',
        'url': 'http://xe.com/currency/?currency=lsl-basotho-loti'},
    'LYD': {
        'symbol': '',
        'name': 'Libya Dinar',
        'url': 'http://xe.com/currency/?currency=lyd-libyan-dinar'},
    'MAD': {
        'symbol': '',
        'name': 'Morocco Dirham',
        'url': 'http://xe.com/currency/?currency=mad-moroccan-dirham'},
    'MDL': {
        'symbol': '',
        'name': 'Moldova Leu',
        'url': 'http://xe.com/currency/?currency=mdl-moldovan-leu'},
    'MGA': {
        'symbol': '',
        'name': 'Madagascar Ariary',
        'url': 'http://xe.com/currency/?currency=mga-malagasy-ariary'},
    'MKD': {
        'symbol': 'ден',
        'name': 'Macedonia Denar',
        'url': 'http://xe.com/currency/?currency=mkd-macedonian-denar'},
    'MMK': {
        'symbol': '',
        'name': 'Myanmar (Burma) Kyat',
        'url': 'http://xe.com/currency/?currency=mmk-burmese-kyat'},
    'MNT': {
        'symbol': '₮',
        'name': 'Mongolia Tughrik',
        'url': 'http://xe.com/currency/?currency=mnt-mongolian-tughrik'},
    'MOP': {
        'symbol': '',
        'name': 'Macau Pataca',
        'url': 'http://xe.com/currency/?currency=mop-macau-pataca'},
    'MRO': {
        'symbol': '',
        'name': 'Mauritania Ouguiya',
        'url': 'http://xe.com/currency/?currency=mro-mauritanian-ouguiya'},
    'MUR': {
        'symbol': '₨',
        'name': 'Mauritius Rupee',
        'url': 'http://xe.com/currency/?currency=mur-mauritian-rupee'},
    'MVR': {
        'symbol': '',
        'name': 'Maldives (Maldive Islands) Rufiyaa',
        'url': 'http://xe.com/currency/?currency=mvr-maldivian-rufiyaa'},
    'MWK': {
        'symbol': '',
        'name': 'Malawi Kwacha',
        'url': 'http://xe.com/currency/?currency=mwk-malawian-kwacha'},
    'MXN': {
        'symbol': '$',
        'name': 'Mexico Peso',
        'url': 'http://xe.com/currency/?currency=mxn-mexican-peso'},
    'MYR': {
        'symbol': 'RM',
        'name': 'Malaysia Ringgit',
        'url': 'http://xe.com/currency/?currency=myr-malaysian-ringgit'},
    'MZN': {
        'symbol': 'MT',
        'name': 'Mozambique Metical',
        'url': 'http://xe.com/currency/?currency=mzn-mozambican-metical'},
    'NAD': {
        'symbol': '$',
        'name': 'Namibia Dollar',
        'url': 'http://xe.com/currency/?currency=nad-namibian-dollar'},
    'NGN': {
        'symbol': '₦',
        'name': 'Nigeria Naira',
        'url': 'http://xe.com/currency/?currency=ngn-nigerian-naira'},
    'NIO': {
        'symbol': 'C$',
        'name': 'Nicaragua Cordoba',
        'url': 'http://xe.com/currency/?currency=nio-nicaraguan-cordoba'},
    'NOK': {
        'symbol': 'kr',
        'name': 'Norway Krone',
        'url': 'http://xe.com/currency/?currency=nok-norwegian-krone'},
    'NPR': {
        'symbol': '₨',
        'name': 'Nepal Rupee',
        'url': 'http://xe.com/currency/?currency=npr-nepalese-rupee'},
    'NZD': {
        'symbol': '$',
        'name': 'New Zealand Dollar',
        'url': 'http://xe.com/currency/?currency=nzd-new-zealand-dollar'},
    'OMR': {
        'symbol': '﷼',
        'name': 'Oman Rial',
        'url': 'http://xe.com/currency/?currency=omr-omani-rial'},
    'PAB': {
        'symbol': 'B/.',
        'name': 'Panama Balboa',
        'url': 'http://xe.com/currency/?currency=pab-panamanian-balboa'},
    'PEN': {
        'symbol': 'S/.',
        'name': 'Peru Nuevo Sol',
        'url': 'http://xe.com/currency/?currency=pen-peruvian-nuevo-sol'},
    'PGK': {
        'symbol': '',
        'name': 'Papua New Guinea Kina',
        'url': 'http://xe.com/currency/?currency=pgk-papua-new-guinean-kina'},
    'PHP': {
        'symbol': '₱',
        'name': 'Philippines Peso',
        'url': 'http://xe.com/currency/?currency=php-philippine-peso'},
    'PKR': {
        'symbol': '₨',
        'name': 'Pakistan Rupee',
        'url': 'http://xe.com/currency/?currency=pkr-pakistani-rupee'},
    'PLN': {
        'symbol': 'zł',
        'name': 'Poland Zloty',
        'url': 'http://xe.com/currency/?currency=pln-polish-zloty'},
    'PYG': {
        'symbol': 'Gs',
        'name': 'Paraguay Guarani',
        'url': 'http://xe.com/currency/?currency=pyg-paraguayan-guarani'},
    'QAR': {
        'symbol': '﷼',
        'name': 'Qatar Riyal',
        'url': 'http://xe.com/currency/?currency=qar-qatari-riyal'},
    'RON': {
        'symbol': 'lei',
        'name': 'Romania New Leu',
        'url': 'http://xe.com/currency/?currency=ron-romanian-new-leu'},
    'RSD': {
        'symbol': 'Ди'
                  'н.', 'name': 'Serbia Dinar',
        'url': 'http://xe.com/currency/?currency=rsd-serbian-dinar'},
    'RUB': {
        'symbol': 'руб',
        'name': 'Russia Ruble',
        'url': 'http://xe.com/currency/?currency=rub-russian-ruble'},
    'RWF': {
        'symbol': '',
        'name': 'Rwanda Franc',
        'url': 'http://xe.com/currency/?currency=rwf-rwandan-franc'},
    'SAR': {
        'symbol': '﷼',
        'name': 'Saudi Arabia Riyal',
        'url': 'http://xe.com/currency/?currency=sar-saudi-arabian-riyal'},
    'SBD': {
        'symbol': '$',
        'name': 'Solomon Islands Dollar',
        'url': 'http://xe.com/currency/?currency=sbd-solomon-islander-dollar'},
    'SCR': {
        'symbol': '₨',
        'name': 'Seychelles Rupee',
        'url': 'http://xe.com/currency/?currency=scr-seychellois-rupee'},
    'SDG': {
        'symbol': '',
        'name': 'Sudan Pound',
        'url': 'http://xe.com/currency/?currency=sdg-sudanese-pound'},
    'SEK': {
        'symbol': 'kr',
        'name': 'Sweden Krona',
        'url': 'http://xe.com/currency/?currency=sek-swedish-krona'},
    'SGD': {
        'symbol': '$',
        'name': 'Singapore Dollar',
        'url': 'http://xe.com/currency/?currency=sgd-singapore-dollar'},
    'SHP': {
        'symbol': '£',
        'name': 'Saint Helena Pound',
        'url': 'http://xe.com/currency/?currency=shp-saint-helenian-pound'},
    'SLL': {
        'symbol': '',
        'name': 'Sierra Leone Leone',
        'url': 'http://xe.com/currency/?currency=sll-sierra-leonean-leone'},
    'SOS': {
        'symbol': 'S',
        'name': 'Somalia Shilling',
        'url': 'http://xe.com/currency/?currency=sos-somali-shilling'},
    'SPL': {
        'symbol': '',
        'name': 'Seborga Luigino',
        'url': 'http://xe.com/currency/?currency=spl-seborgan-luigino'},
    'SRD': {
        'symbol': '$',
        'name': 'Suriname Dollar',
        'url': 'http://xe.com/currency/?currency=srd-surinamese-dollar'},
    'STD': {
        'symbol': '',
        'name': 'São Tomé and Príncipe Dobra',
        'url': 'http://xe.com/currency/?currency=std-sao-tomean-dobra'},
    'SVC': {
        'symbol': '$',
        'name': 'El Salvador Colon',
        'url': 'http://xe.com/currency/?currency=svc-salvadoran-colon'},
    'SYP': {
        'symbol': '£',
        'name': 'Syria Pound',
        'url': 'http://xe.com/currency/?currency=syp-syrian-pound'},
    'SZL': {
        'symbol': '',
        'name': 'Swaziland Lilangeni',
        'url': 'http://xe.com/currency/?currency=szl-swazi-lilangeni'},
    'THB': {
        'symbol': '฿',
        'name': 'Thailand Baht',
        'url': 'http://xe.com/currency/?currency=thb-thai-baht'},
    'TJS': {
        'symbol': '',
        'name': 'Tajikistan Somoni',
        'url': 'http://xe.com/currency/?currency=tjs-tajikistani-somoni'},
    'TMT': {
        'symbol': '',
        'name': 'Turkmenistan Manat',
        'url': 'http://xe.com/currency/?currency=tmt-turkmenistani-manat'},
    'TND': {
        'symbol': '',
        'name': 'Tunisia Dinar',
        'url': 'http://xe.com/currency/?currency=tnd-tunisian-dinar'},
    'TOP': {
        'symbol': '',
        'name': "Tonga Pa'anga",
        'url': "http://xe.com/currency/?currency=top-tongan-pa'anga"},
    'TRY': {
        'symbol': '₺',
        'name': 'Turkey Lira',
        'url': 'http://xe.com/currency/?currency=try-turkish-lira'},
    'TTD': {
        'symbol': 'TT$',
        'name': 'Trinidad and Tobago Dollar',
        'url': 'http://xe.com/currency/?currency=ttd-trinidadian-dollar'},
    'TVD': {
        'symbol': '$',
        'name': 'Tuvalu Dollar',
        'url': 'http://xe.com/currency/?currency=tvd-tuvaluan-dollar'},
    'TWD': {
        'symbol': 'NT$',
        'name': 'Taiwan New Dollar',
        'url': 'http://xe.com/currency/?currency=twd-taiwan-new-dollar'},
    'TZS': {
        'symbol': '',
        'name': 'Tanzania Shilling',
        'url': 'http://xe.com/currency/?currency=tzs-tanzanian-shilling'},
    'UAH': {
        'symbol': '₴',
        'name': 'Ukraine Hryvnia',
        'url': 'http://xe.com/currency/?currency=uah-ukrainian-hryvnia'},
    'UGX': {
        'symbol': '',
        'name': 'Uganda Shilling',
        'url': 'http://xe.com/currency/?currency=ugx-ugandan-shilling'},
    'USD': {
        'symbol': '$',
        'name': 'United States Dollar',
        'url': 'http://xe.com/currency/?currency=usd-us-dollar'},
    'UYU': {
        'symbol': '$U',
        'name': 'Uruguay Peso',
        'url': 'http://xe.com/currency/?currency=uyu-uruguayan-peso'},
    'UZS': {
        'symbol': 'лв',
        'name': 'Uzbekistan Som',
        'url': 'http://xe.com/currency/?currency=uzs-uzbekistani-som'},
    'VEF': {
        'symbol': 'Bs',
        'name': 'Venezuela Bolivar',
        'url': 'http://xe.com/currency/?currency=vef-venezuelan-bolivar'},
    'VND': {
        'symbol': '₫',
        'name': 'Viet Nam Dong',
        'url': 'http://xe.com/currency/?currency=vnd-vietnamese-dong'},
    'VUV': {
        'symbol': '',
        'name': 'Vanuatu Vatu',
        'url': 'http://xe.com/currency/?currency=vuv-ni-vanuatu-vatu'},
    'WST': {
        'symbol': '',
        'name': 'Samoa Tala',
        'url': 'http://xe.com/currency/?currency=wst-samoan-tala'},
    'XAF': {
        'symbol': '',
        'name': 'Central African CFA franc',
        'url': 'http://xe.com/currency/?currency=xaf-central-african-cfa-franc-beac'},
    'XCD': {
        'symbol': '$',
        'name': 'East Caribbean Dollar',
        'url': 'http://xe.com/currency/?currency=xcd-east-caribbean-dollar'},
    'XOF': {
        'symbol': '',
        'name': 'West African CFA Franc',
        'url': 'http://xe.com/currency/?currency=xof-cfa-franc'},
    'XPF': {
        'symbol': '',
        'name': 'CFP Franc',
        'url': 'http://xe.com/currency/?currency=xpf-cfp-franc'},
    'YER': {
        'symbol': '﷼',
        'name': 'Yemen Rial',
        'url': 'http://xe.com/currency/?currency=yer-yemeni-rial'},
    'ZAR': {
        'symbol': 'R',
        'name': 'South Africa Rand',
        'url': 'http://xe.com/currency/?currency=zar-south-african-rand'},
    'ZMW': {
        'symbol': '',
        'name': 'Zambia Kwacha',
        'url': 'http://xe.com/currency/?currency=zmw-zambian-kwacha'},
    'ZWD': {
        'symbol': 'Z$',
        'name': 'Zimbabwe Dollar',
        'url': 'http://xe.com/currency/?currency=zwd-zimbabwean-dollar'}
}


# COMMANDS
# ---------------------------------------------------------------------------------------------------------------------#
class Command(BaseCommand):
    help = "Sync FactBook with external APIs!"

    def handle(self, *args, **options):

        logger.info('Erasing data...')
        Country.objects.all().delete()
        Currency.objects.all().delete()
        # TODO: optionally clear all data...

        logger.info('Getting currency data...')
        # url = 'https://gist.githubusercontent.com/Fluidbyte/2973986/raw/' \
        # '9ead0f85b6ee6071d018564fa5a314a0297212cc/Common-Currency.json'
        # response = requests.get(url)

        # for key, value in response.json().items():
        for key, value in CURRENCIES.items():
            logger.info(value)

            currency = Currency(
                name=value.get('name'),
                symbol=value.get('symbol'),
                code=key,
            )

            currency.save()

        logger.info('Getting country data...')
        response = requests.get('http://restcountries.eu/rest/v1/all')

        for data in response.json():
            logger.info(data.get('name'))
            continent, created = Continent.objects.get_or_create(name=data.get('region'))
            region, created = Region.objects.get_or_create(name=data.get('subregion'))

            try:
                country = Country.objects.get_by_natural_key(data.get(('name', )))
                logger.info('Found country, updating...')
                # TODO: Update the Country!

            except Country.DoesNotExist:
                country = Country(
                    name=data.get('name'),
                    alpha3code=data.get('alpha3Code'),
                    alpha2code=data.get('alpha2Code'),
                    continent=continent,
                    region=region,
                    population=data.get('population'),
                    demonym=data.get('demonym'),
                    native_name=data.get('nativeName'),
                )

                display_info = COUNTRIES.get(data.get('alpha2Code'))
                if display_info:
                    country.display_name = display_info.get('display_name')
                    country.position = display_info.get('position')
            finally:
                country.save()

        logger.info('Done')