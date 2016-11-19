#!/bin/bash

wget -qO - http://www.yandex.ru| grep -oE 'link_black_yes" aria-label="[^"]+"'> text1; cat text1| sed -e 's/link_black_yes" aria-label=//g'> last_info; cat last_info; rm text1;
