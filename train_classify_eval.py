from Preprocessing import load_dataset
from Train import Train
from Classification import SpamClassification
from Evaluation import*


# load data
easy_ham, spam = load_dataset(data_preprocessed=True)

# chuan bi du lieu va nhan
samples = easy_ham + spam
labels = [SpamClassification.HAM] * (len(easy_ham)) + [SpamClassification.SPAM] * len(spam)

# ti le tap train
train_ratio = 0.66

# ti le tap val
val_ratio = 0

# Tron du lieu va chia tap du lieu thanh cac tap train, val, test
x_train, x_val, x_test, y_train, y_val, y_test = datas_split(samples, labels, train_ratio, val_ratio)

# Train
train = Train(x_train, y_train)

#%%
# epsilon
e = 0

# Classify
classifier = SpamClassification(train.P, train.P_ti, train.T, e)

# predict test data
predicted_y_test = classifier.classify_D_test(x_test)


# Evaluation
print("accuracy: {:.5f}\n".format(accuracy(y_test, predicted_y_test)))

confusion_matrix(y_test, predicted_y_test, Train.SPAM)

print("\nprecision_spam: {:.5f}\n".format(precision(y_test, predicted_y_test, Train.SPAM)))

print("\nrecall_spam: {:.5f}\n".format(recall(y_test, predicted_y_test, Train.SPAM)))

print("\nprecision_ham: {:.5f}\n".format(precision(y_test, predicted_y_test, Train.HAM)))

print("\nrecall_ham: {:.5f}\n".format(recall(y_test, predicted_y_test, Train.HAM)))

print("Macro_averaging: {:.5f}".format(Macro_averaging(y_test, predicted_y_test)))

#%%

# Classfy spam

mail = '''From 12a1mailbot1@web.de  Thu Aug 22 13:17:22 2002
Return-Path: <12a1mailbot1@web.de>
Delivered-To: zzzz@localhost.example.com
Received: from localhost (localhost [127.0.0.1])
	by phobos.labs.example.com (Postfix) with ESMTP id 136B943C32
	for <zzzz@localhost>; Thu, 22 Aug 2002 08:17:21 -0400 (EDT)
Received: from mail.webnote.net [193.120.211.219]
	by localhost with POP3 (fetchmail-5.9.0)
	for zzzz@localhost (single-drop); Thu, 22 Aug 2002 13:17:21 +0100 (IST)
Received: from dd_it7 ([210.97.77.167])
	by webnote.net (8.9.3/8.9.3) with ESMTP id NAA04623
	for <zzzz@example.com>; Thu, 22 Aug 2002 13:09:41 +0100
From: 12a1mailbot1@web.de
Received: from r-smtp.korea.com - 203.122.2.197 by dd_it7  with Microsoft SMTPSVC(5.5.1775.675.6);
	 Sat, 24 Aug 2002 09:42:10 +0900
To: <dcek1a1@netsgo.com>
Subject: Life Insurance - Why Pay More?
Date: Wed, 21 Aug 2002 20:31:57 -1600
MIME-Version: 1.0
Message-ID: <0103c1042001882DD_IT7@dd_it7>
Content-Type: text/html; charset="iso-8859-1"
Content-Transfer-Encoding: quoted-printable

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML><HEAD>
<META content=3D"text/html; charset=3Dwindows-1252" http-equiv=3DContent-T=
ype>
<META content=3D"MSHTML 5.00.2314.1000" name=3DGENERATOR></HEAD>
<BODY><!-- Inserted by Calypso -->
<TABLE border=3D0 cellPadding=3D0 cellSpacing=3D2 id=3D_CalyPrintHeader_ r=
ules=3Dnone 
style=3D"COLOR: black; DISPLAY: none" width=3D"100%">
  <TBODY>
  <TR>
    <TD colSpan=3D3>
      <HR color=3Dblack noShade SIZE=3D1>
    </TD></TR></TD></TR>
  <TR>
    <TD colSpan=3D3>
      <HR color=3Dblack noShade SIZE=3D1>
    </TD></TR></TBODY></TABLE><!-- End Calypso --><!-- Inserted by Calypso=
 --><FONT 
color=3D#000000 face=3DVERDANA,ARIAL,HELVETICA size=3D-2><BR></FONT></TD><=
/TR></TABLE><!-- End Calypso --><FONT color=3D#ff0000 
face=3D"Copperplate Gothic Bold" size=3D5 PTSIZE=3D"10">
<CENTER>Save up to 70% on Life Insurance.</CENTER></FONT><FONT color=3D#ff=
0000 
face=3D"Copperplate Gothic Bold" size=3D5 PTSIZE=3D"10">
<CENTER>Why Spend More Than You Have To?
<CENTER><FONT color=3D#ff0000 face=3D"Copperplate Gothic Bold" size=3D5 PT=
SIZE=3D"10">
<CENTER>Life Quote Savings
<CENTER>
<P align=3Dleft></P>
<P align=3Dleft></P></FONT></U></I></B><BR></FONT></U></B></U></I>
<P></P>
<CENTER>
<TABLE border=3D0 borderColor=3D#111111 cellPadding=3D0 cellSpacing=3D0 wi=
dth=3D650>
  <TBODY></TBODY></TABLE>
<TABLE border=3D0 borderColor=3D#111111 cellPadding=3D5 cellSpacing=3D0 wi=
dth=3D650>
  <TBODY>
  <TR>
    <TD colSpan=3D2 width=3D"35%"><B><FONT face=3DVerdana size=3D4>Ensurin=
g your 
      family's financial security is very important. Life Quote Savings ma=
kes 
      buying life insurance simple and affordable. We Provide FREE Access =
to The 
      Very Best Companies and The Lowest Rates.</FONT></B></TD></TR>
  <TR>
    <TD align=3Dmiddle vAlign=3Dtop width=3D"18%">
      <TABLE borderColor=3D#111111 width=3D"100%">
        <TBODY>
        <TR>
          <TD style=3D"PADDING-LEFT: 5px; PADDING-RIGHT: 5px" width=3D"100=
%"><FONT 
            face=3DVerdana size=3D4><B>Life Quote Savings</B> is FAST, EAS=
Y and 
            SAVES you money! Let us help you get started with the best val=
ues in 
            the country on new coverage. You can SAVE hundreds or even tho=
usands 
            of dollars by requesting a FREE quote from Lifequote Savings. =
Our 
            service will take you less than 5 minutes to complete. Shop an=
d 
            compare. SAVE up to 70% on all types of Life insurance! 
</FONT></TD></TR>
        <TR><BR><BR>
          <TD height=3D50 style=3D"PADDING-LEFT: 5px; PADDING-RIGHT: 5px" 
          width=3D"100%">
            <P align=3Dcenter><B><FONT face=3DVerdana size=3D5><A 
            href=3D"http://website.e365.cc/savequote/">Click Here For Your=
 
            Free Quote!</A></FONT></B></P></TD>
          <P><FONT face=3DVerdana size=3D4><STRONG>
          <CENTER>Protecting your family is the best investment you'll eve=
r 
          make!<BR></B></TD></TR>
        <TR><BR><BR></STRONG></FONT></TD></TR></TD></TR>
        <TR></TR></TBODY></TABLE>
      <P align=3Dleft><FONT face=3D"Arial, Helvetica, sans-serif" size=3D2=
></FONT></P>
      <P></P>
      <CENTER><BR><BR><BR>
      <P></P>
      <P align=3Dleft><BR></B><BR><BR><BR><BR></P>
      <P align=3Dcenter><BR></P>
      <P align=3Dleft><BR></B><BR><BR></FONT>If you are in receipt of this=
 email 
      in error and/or wish to be removed from our list, <A 
      href=3D"mailto:coins@btamail.net.cn">PLEASE CLICK HERE</A> AND TYPE =
REMOVE. If you 
      reside in any state which prohibits e-mail solicitations for insuran=
ce, 
      please disregard this 
      email.<BR></FONT><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR><BR=
><BR><BR><BR></FONT></P></CENTER></CENTER></TR></TBODY></TABLE></CENTER></=
CENTER></CENTER></CENTER></CENTER></BODY></HTML>



'''
print(classifier.classify(mail))

