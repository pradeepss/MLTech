# you can use homeutil command
#
# 1. For write: homeutil write-value -h $homeName -a "$accessoryName" -r $serviceID -c $charID -i $currentValue
# 2. For read: homeutil read-value -h $homeName -a "$accessoryName" -r $serviceID -c $charID
#
#
# I have following shell script too, but i have to show you how to use it or copy paste this line into your device:
#
# rm /var/root/.performanceProfile
# # To enter vi, type: vi filename <Return> and then type <i> to enter into insert mode.
# vi /var/root/.performanceProfile
#
# i
# clear


#Local Variables
TIMEFORMAT=%R
WiFiidleTime=600
BTidleTime=15  #BT idle time 10 seconds
Iteration=20
WiFiIteration=3
randomSleep=8

function pairing()
{
    echo "=========================Pairing $accessoryName============="  >> /var/tmp/logPerfromance.csv
rm /tmp/hkCommands
echo browse-start >> /tmp/hkCommands #DirectCall doesn't work
echo sleep -s 5 >> /tmp/hkCommands
read -p "Enter Setup Code: "  setupCode
echo add-acc -n \"$accessoryName\" -h $homeName -p $setupCode >> /tmp/hkCommands
for number in $(seq $Iteration)
do
echo "Iteration: " $number
(time homeutil execute -f /tmp/hkCommands ) 2>>/var/tmp/logPerfromance.csv
sleep $randomSleep
homeutil remove-accessory -h $homeName -n "$accessoryName"
sleep $randomSleep
done

}


function readValue()
{

    echo "=========================Reading Values for $accessoryName=============" >> /var/tmp/logPerfromance.csv
echo
sum=0
value=0
homeutil read-value -h $homeName -a "$accessoryName" -r $serviceID -c $charID
sleep $randomSleep
for number in $(seq $Iteration)
do
echo "Iteration: " $number
#value = $((time homeutil read-value -h $homeName -a "$accessoryName" -r $serviceID -c $charID) 2>&1)
(time homeutil read-value -h $homeName -a "$accessoryName" -r $serviceID -c $charID) 2>>/var/tmp/logPerfromance.csv
sleep $randomSleep
#echo $value >> /var/tmp/logPerfromance.csv
#$sum=$sum+$value
done
#avg=$sum/$Iteration
#echo $avg
#echo "Average: " $avg

}

function writeValue()
{
    echo "=========================Writing Values for $accessoryName============="  >> /var/tmp/logPerfromance.csv
echo
currentValue=0
#Initialization
homeutil write-value -h $homeName -a "$accessoryName" -r $serviceID -c $charID -i $currentValue
sleep $randomSleep
for number in $(seq $Iteration)
do
echo "Iteration: " $number
echo "CurrentValue : " $currentValue
currentValue=$((currentValue==0))
(time homeutil write-value -h $homeName -a "$accessoryName" -r $serviceID -c $charID -i $currentValue) 2>>/var/tmp/logPerfromance.csv
sleep $randomSleep
done
}

function btreadValue()
{
    echo "======================BTLE Idle Reading Values for $accessoryName======"  >> /var/tmp/logPerfromance.csv
sleep $BTidleTime
for number in $(seq $Iteration)
do
echo "Iteration: " $number
(time homeutil read-value -h $homeName -a "$accessoryName" -r $serviceID -c $charID) 2>>/var/tmp/logPerfromance.csv
sleep $BTidleTime
done
}

function btwriteValue()
{
    echo "==================BTLE Idle Writing Values for $accessoryName=========="  >> /var/tmp/logPerfromance.csv
echo
currentValue=0
#Initialization
homeutil write-value -h $homeName -a "$accessoryName" -r $serviceID -c $charID -i $currentValue
sleep $BTidleTime

for number in $(seq $Iteration)
do
echo "Iteration: " $number
echo "CurrentValue : " $currentValue
currentValue=$((currentValue==0))
(time homeutil write-value -h $homeName -a "$accessoryName" -r $serviceID -c $charID -i $currentValue) 2>>/var/tmp/logPerfromance.csv
sleep $BTidleTime
done
}

function longidle()
{
    echo "=================10 minutes idle Writing Values for $accessoryName======="  >> /var/tmp/logPerfromance.csv
currentValue=0
#Initialization
homeutil write-value -h $homeName -a "$accessoryName" -r $serviceID -c $charID -i $currentValue
sleep $randomSleep
for number in $(seq $WiFiIteration)
do
echo "Iteration: " $number
echo "CurrentValue : " $currentValue
currentValue=$((currentValue==0))
(time homeutil write-value -h $homeName -a "$accessoryName" -r $serviceID -c $charID -i $currentValue) 2>>/var/tmp/logPerfromance.csv
sleep $WiFiidleTime
done
}

function disconnectWiFi()
{
    echo "=========================Going Remote==========================="
mobilewifitool -- manager power 0
sleep 10
#wl -i en0 status
echo "======================Going Remote Complete======================"
#read -p "Wait for Confirmation to Proceed(y/q): " proceed
#if [ "$proceed" = "q" ]; then
#	echo "Exiting test…"
#	exit
#elif [ "$opt" = "y" ]; then
#	sleep 15
#fi

}

function connectWiFi()
{
    echo "=========================Connecting WiFi again======================"
mobilewifitool -- manager power 1
sleep 10
#wl -i en0 status
echo "======================WiFi Connected============================="
#read -p "Wait for Confirmation to Proceed(y/q): " proceed
#if [ "$proceed" = "q" ]; then
#	echo "Exiting test…"
#	exit
#elif [ "$proceed" = "y" ]; then
#	sleep 15
#else
#	clear
#	echo bad option
#fi
}


function show_menu()
{
    echo "=========================Test Option=============================="
echo "1.	Read Values"
echo "2.	Write Values"
echo "3.	BT Read Values"
echo "4.	BT Write Values"
echo "5.	10 min idle Write Values"
echo "6.	Accessory Pairing"
echo "ip.	All IP tests"
echo "bt.	All BT tests"
echo

}

function starttest()
{
    echo "=========================Starting test==============================="
rm /var/tmp/logPerfromance.csv
mobilewifitool -- manager power 1
echo "Welcome to HomeKit Performance Tester v0.1"
echo "File bugs to : Purple HomeKit Tools | 1.0, Component: Performance"
read -p "Number of Iterations: " Iteration
read -p "Enter Home Name: "  homeName
homeutil add-home -n $homeName
# check for existing home
while true;
do
show_menu
read -p "Enter your choice, or q for exit: " opt
echo
if [ "$opt" = "q" ]; then
echo "Exiting test…"
break
fi
read -p "Enter Accessory Name: "  accessoryName
if [ "$opt" -ne 6 ]; then
read -p "Enter Service ID: "  serviceID
read -p "Enter Characteristic ID: "  charID
fi
if [ "$opt" -eq 1 ]; then
readValue
elif [ "$opt" -eq 2 ]; then
writeValue
elif [ "$opt" -eq 3 ]; then
btreadValue
elif [ "$opt" -eq 4 ]; then
btwriteValue
elif [ "$opt" -eq 5 ]; then
longidle
elif [ "$opt" -eq 6 ]; then
pairing
elif [ "$opt" ="ip" ]; then
readValue
sleep 5
writeValue
sleep 5
disconnectWiFi
sleep 5
readValue
sleep 5
writeValue
sleep 5
longidle
sleep 5
connectWiFi
elif [ "$opt" = "bt" ]; then
readValue
sleep 5
writeValue
sleep 5
btreadValue
sleep 5
btwriteValue
sleep 5
disconnectWiFi
sleep 5
readValue
sleep 5
writeValue
sleep 5
btreadValue
sleep 5
btwriteValue
sleep 5
connectWiFi
else
clear
echo bad option
fi
done
}

#To leave insert mode and return to command mode, press: <Esc>

:wq