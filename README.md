# ClassificationSpam

# Thư viện sử dụng: gensim
* Cài đặt: 
```
pip install gensim
```

# Cài đặt/biên dịch/chạy chương trình

Triển khai trên [COLAP](https://colab.research.google.com/drive/1dOfIfInPU9wL0EjSz8DxCVYMnZU8WsDO#scrollTo=aZ4pPSXTopv-)

* Cài đặt
```
import os
import sys

# Download source code.
if "ClassificationSpam" not in os.getcwd():
  git clone --depth 1 https://github.com/wind123mountain/ClassificationSpam
  os.chdir('ClassificationSpam')
  sys.path.append('.')
else:
  git pull
```

* Khởi tạo module
```
import module
classify = module.create_modul()
```

* Phân loại thư mới

```
import 

mail = '''Received: from linux.midrange.com (dial-62-64-223-40.access.uk.tiscali.com [62.64.223.40])
	by linux.midrange.com (8.11.6/8.11.6) with SMTP id g6IDvRt21715
	for <gibbs@midrange.com>; Thu, 18 Jul 2002 08:57:28 -0500
Message-Id: <200207181357.g6IDvRt21715@linux.midrange.com>
From: "your long lost friend" <justokandgroovy@kunmail.com>
Date: Thu, 18 Jul 2002 14:58:29
To: gibbs@midrange.com
Subject: A rare and wonderful email really!
MIME-Version: 1.0
Content-Type: text/plain;charset="iso-8859-1"
Content-Transfer-Encoding: 7bit
X-Status: 
X-Keywords: 

Hi we are luke's secret following we love luke fictitious!

We are also your long lost friend! Hi

This email has nothing to do with lukefictitious.com

We wil be putting up our very own fan site soon
and wanted to let you know in advance!

Have a beautifull day!


'''

res = classify.classify(mail)
if (res == Classification.SpamClassification.SPAM):
  print('SPAM')
else:
  print('HAM')
  
```
