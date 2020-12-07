# sdlm-cli
Download your serial files with **s**erial **d**own**l**oad **m**anager so easy. You just get your one episode download link of your film on any season to command line and it makes your episode that you want and make a file to store them and you can download it with *aria2c* or *sdlm* cli.


# How to install on my device?
Still working on it. I'll release *sdlm* soon. But you can use it with run this python script.

```
python main.py
```
If you want to download, please do not forget install **aria2c** on your system. You can install it with *apt* like this:

```
# apt install aria2c
```

That's it :smiley:!


# How to use commands
* **Add new serial link**
<br> To add new serial link to sdlm you have *add* paramet on your cli and then it ask 3 questions. On its first question, it ask and want your serial link. Second question is your current Episode on your link. And third question is your last Episode of your serial. Then sdlm try to make your links and put them on a file named *.sdlm-links.txt*.
<br><br>
![Demo of your bash](https://s16.picofile.com/file/8416626476/carbon.png)

* **Start Download**
<br> To start download your files, you can use *aria2c* or just be on your folder that add link (Need *.sdlm-links.txt*).
<br><br>
![Demo if your bash](https://s16.picofile.com/file/8416626492/carbon_1_.png")

# Todo
I have to make this project comple and better or **YOU** can help me to do this to together.

[ ] Manage download with *aria2p*

[ ] Make add link easier and better

[ ] Put this script on apt package manager and more.

[*] Make first release (Dec 7 2020)