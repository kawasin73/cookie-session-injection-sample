# cookie-session-injection-sample

[Randall Degges - Please Stop Using Local Storage](https://www.rdegges.com/2018/please-stop-using-local-storage/) says that save secrets at Session with cookie not at local Storage.

But secrets saved at session will leak even when javascript from other origin injected so that i think this article is meanless.

In Japanese : [HTML5のLocal Storageを使ってはいけない（翻訳）](https://techracho.bpsinc.jp/hachi8833/2019_10_09/80851)

```bash
$ git clone https://github.com/kawasin73/cookie-session-injection-sample.git
$ cd cookie-session-injection-sample
$ pipenv install
$ export FLASK_APP=view.py
$ pipenv run flask run
```

```bash
# on macOS add hosts
$ sudo vi /private/etc/hosts

127.0.0.1 invalid.local
127.0.0.1 success.local2

$ sudo killall -HUP mDNSResponder
```

1. access `http://success.local2:5000`
2. write some value to form and submit
3. show developer console
4. click `fetchValue` button which send `/value` request and get session value
5. click `getInvalid` button and execute `getInvalid()` which from other site javascript (injected code)
6. `getInvalid()` will receive session secret value!!!

## LICENSE

MIT
