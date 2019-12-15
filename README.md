Ссылка на курс "Автоматизация UI-тестирования на Python" - https://stepik.org/course/58297/syllabus


==============================Linux_OS_Settings==============================
1. Установить python 3.7:

        ```bash
        sudo apt-get update
        sudo apt-get upgrade
        sudo apt-get install python3.7
        ```

2. Установить pip:

        ```bash
        python3 -m pip install pip
        ```

3. Создать виртуальное окружение:

        ```bash
        sudo apt-get install -y python3.7-venv
        mkdir ~/env
        cd ~/env
        python3.7 -m venv py_3_7
        ```

4. Активировать виртуальное окружение:

        ```bash
        cd ~/env
        source py_3_7/bin/activate
        ```

5. Установить необходимые библиотеки:

        ```bash
        pip install -r requirements.txt
        ```

6. Установить JAVA для формирования отчётов с помощью allure:

        ```bash
        sudo apt-get install default-jre
        sudo apt-get install default-jdk
        ```
Проверить, что JAVA установлена:

        ```bash
        java -version
        ```

В консоли должна отобразится установленная версия, например:
openjdk version "1.8.0_222"


7. Задать переменную JAVA_HOME:

        ```bash
        sudo gedit /etc/profile
        ```

В конец файла добавить (для переменной JAVA_HOME должен быть указан верный путь до установленного jdk):

JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
PATH=$PATH:$HOME/bin:$JAVA_HOME/bin
export JAVA_HOME
export JRE_HOME
export PATH

Для применения настроек перезагрузиться:

        ```bash
        reboot
        ```

После перезагрузки проверить, что переменная JAVA_HOME задана:

        ```bash
        echo $JAVA_HOME
        ```

Если всё верно, должен отобразиться заданный путь, например:
/usr/lib/jvm/java-8-openjdk-amd64


8. Установить Allure:

        ```bash
        sudo apt-add-repository ppa:qameta/allure
        sudo apt-get update
        sudo apt-get install allure
        ```

Скачать архив .tgz последней версии allure с сайта:
http://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/

# curl -o allure-2.6.0.tgz -Ls https://dl.bintray.com/qameta/generic/io/qameta/allure/allure/2.6.0/allure-2.6.0.tgz

        ```bash
        sudo tar -zxvf allure-2.13.0.tgz -C /opt/
#        sudo ln -s /opt/allure-2.6.0/bin/allure /usr/bin/allure
        allure --version
        ```
или скачать архив --> разархивировать в папку --> добавить папку bin из содержимого, извлеченного из архива, в PATH. 
Путь к нужной нам папке выглядит примерно так (именно его и нужно добавить в PATH):
.../allure-2.13.0/bin/

9. Установить allure для PyTest:

        ```bash
        pytest install allure-pytest
        ```

10. В папке с тестами создать папку для генерации отчётов allure:

        ```bash
        mkdir /<path_to_tests>/my_allure_reports
        ```

11. Запустить тест из тест-комплекта командой:

        ```bash
        pytest --alluredir=/<path_to_tests>/my_allure_reports <test_name>.py
        ```

12. "Собрать" репорт командой:

        ```bash
        allure serve /<path_to_tests>/my_allure_reports
        ```

В ответ на эту команду автоматически откроется новая вкладка Chrome, в которой будет отображена HTML-страница, расположенная на локальном хосте, с результатами прохождения тестов, запущенных на шаге 11.


13. Запустить тест с формированием отчёта в allure:

        ```bash
        pytest --browser=Chrome --alluredir=/<path_to_tests>/my_allure_reports test_make_report.py
        ```

14. После завершения работы можно деактировать виртуальное окружение:

        ```bash
        deactivate
        ```

	
