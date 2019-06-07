{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "working hours...\n",
      "working hours...\n",
      "working hours...\n",
      "working hours...\n",
      "working hours...\n"
     ]
    },
    {
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-8-e72c4025ea4d>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m     29\u001b[0m             \u001b[0mfile\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtruncate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     30\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 31\u001b[1;33m     \u001b[0mtime\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: "
     ]
    }
   ],
   "source": [
    "import time\n",
    "from datetime import datetime as dt\n",
    "hosts_path=r\"C:\\Windows\\System32\\drivers\\etc\\hosts\"\n",
    "hosts_temp=\"hosts\"\n",
    "redirect=\"127.0.0.1\"\n",
    "website_list=[\"https://www.tutorialspoint.com\",\"tutorialspoint.com\",\"ankitap2.ias.com\",\"mayank-am.ias.com\",\"https://in.linkedin.com/\",\"in.linkedin.com\"]\n",
    "\n",
    "while True:\n",
    "    if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,16):    \n",
    "        print(\"working hours...\")\n",
    "        with open(hosts_temp,'r+')as file:\n",
    "            \n",
    "            content=file.read()\n",
    "            #print(content)\n",
    "            for website in website_list:\n",
    "                if website in content:\n",
    "                    pass\n",
    "                else:\n",
    "                    file.write(redirect+\" \"+website+\"\\n\")\n",
    "                    \n",
    "    else:\n",
    "        print(\"fun time\")\n",
    "        with open(hosts_path,\"r+\")as file:\n",
    "            content=file.readlines()\n",
    "            file.seek(0)\n",
    "            for line in content:\n",
    "                if not any(website in line for website in website_list):\n",
    "                    file.write(line)\n",
    "            file.truncate()\n",
    "        \n",
    "    time.sleep(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
