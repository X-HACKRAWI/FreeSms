#!/usr/bin/env bash
clear
echo -e "\e[4;31m Yemen Shield !!! \e[0m"
echo -e "\e[1;32m Presents \e[0m"
echo -e "\e[1;34m"
figlet -f slant X-SMS
echo "Press Enter To Launch"
read a1
if [[ -s update.shield.yemen ]];then
echo "All Requirements Found...."
else
echo 'Installing Requirements....'
echo .
echo .
apt install figlet toilet python curl ruby -y
apt install python3-pip
gem install lolcat
echo This Tool Is Created By X-HACKRAWI
echo This Script Is Created By Yemen Shield X-HACKRAWI >update.shield.yemen
echo Requirements Installed....
echo Press Enter To Continue...
read upd
fi
while :
do
rm *.xxx >/dev/null 2>&1
clear
echo -e "\e[1;31m"
figlet -f slant X-SMS| lolcat
echo -e "\e[1;34m Created By \e[1;32m"  #blue color
toilet -f mono12 -F border X-HACKRAWI | lolcat
echo -e "\e[4;34mThis Tool Is Created By Yemen Shield  \e[0m" #underline+blue
echo -e "\e[1;34mFor Any Queries !!!\e[0m"
echo -e "\e[1;32m        instagram: https://www.instagram.com/hackrawi11/ \e[0m" #yellow
echo -e "\e[1;34m    Telegram: https://t.me/Yemen_Shield \e[0m"
echo " "
echo -e "\e[4;31mRead Instruction Carefully !!! \e[0m" #red
echo " "
echo "Enter 1 To  Run X-SMS"
echo "Enter 2 To  Track X-SMS"  #white
echo "Enter 3 To  Update "
echo "Enter 4 To  Check Features "
echo "Enter 5 To  Exit "
read ch
if [ $ch -eq 1 ];then
clear
echo -e "\e[1;32m"
rm *.xxx >/dev/null 2>&1
python3 fakesms.py
rm *.xxx >/dev/null 2>&1
exit 0
elif [ $ch -eq 2 ];then
clear
echo -e "\e[1;32m"
echo 'Track X-SMS'> call.xxx
python3 fakesms.py track
rm *.xxx >/dev/null 2>&1
exit 0
elif [ $ch -eq 3 ];then
clear
apt install git -y
echo -e "\e[1;34m Requesting Update From Source..."
echo -e "\e[1;34m Request Attempt Successful.."
echo -e "\e[1;34m Updating Now..."
git clone https://github.com/X-HACKRAWI/FreeSms.git
if [[ -s FreeSms/Run.sh ]];then
cd FreeSms
cp -r -f * .. > temp
cd ..
rm -rf  FreeSms>> temp
rm update.shield.yemen>> temp
rm temp
chmod +x Run.sh
fi
echo -e "\e[1;32m X-SMS Will Refresh Now..."
echo -e "\e[1;32m All The Required Packages Have Been Installed..."
echo -e "\e[1;34m Press Enter To Refresh..."
read a6
./Run.sh
exit
elif [ $ch -eq 4 ];then
clear
echo -e "\e[1;33m"
figlet -f slant X-SMS| lolcat
echo -e "\e[1;34mCreated By \e[1;34m"  #Blue Color
toilet -f mono12 -F border X-HACKRAWI | lolcat
echo  " "
echo -e "\e[1;32m                   Features\e[1;34m"
echo "  Ultra-Fast-Smooth Sending"
echo "  International Sending"
echo "  Tracking "
echo "  Automatic Future Updates"
echo "  Easy To Use And Embed in Code"
echo ""
echo ""
echo -e "\e[1;31m This is Only For Educational Purposes or To Prank.\e[0m"
echo -e "\e[1;31m Do not Use This To Irritate Others. \e[0m"
echo -e "\e[1;31m Do not Use This To Harm Others. \e[0m"
echo -e "\e[1;31m We Are Not Responsible For The Misuse Of The Script. \e[0m"
echo -e "\e[1;32m Update If Doesn't Work.\e[0m"
echo  " "
echo "Press Enter To Return To Main Menu"
read a3
clear
elif [ $ch -eq 5 ];then
clear
echo -e "\e[1;31m"
figlet -f slant X-SMS| lolcat
echo -e "\e[1;34m Created By \e[1;32m"
toilet -f pagga -F border X-HACKRAWI | lolcat
echo -e "\e[1;34mFor Any Queries !!!\e[0m"
echo -e "\e[1;32m        instagram: https://www.instagram.com/hackrawi11/ \e[0m" #yellow
echo -e "\e[1;34m    Telegram: https://t.me/Yemen_Shield \e[0m"
echo " "
exit 0
else
echo -e "\e[4;32m Invalid Input Detected !!! \e[0m"
echo "Press Enter To Return To Main Menu"
read a3
clear
fi
done