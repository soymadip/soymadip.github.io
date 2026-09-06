FROM phpmyadmin:latest

RUN apt-get update \
    && apt-get install -y --no-install-recommends wget unzip \
    && wget -O /tmp/boodark.zip \
       https://files.phpmyadmin.net/themes/boodark/1.2.0/boodark-1.2.0.zip \
    && unzip /tmp/boodark.zip -d /var/www/html/themes \
    && mv /var/www/html/themes/boodark/css/theme.css \
           /var/www/html/themes/boodark/css/theme-cyan.css \
    && mv /var/www/html/themes/boodark/css/theme-nord.css \
           /var/www/html/themes/boodark/css/theme.css \
    && rm /tmp/boodark.zip \
    && apt-get purge -y wget unzip \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*