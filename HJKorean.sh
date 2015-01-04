case "$1" in 
    start)
	echo "=========================================Starting HJKorean Server============================================"
	nohup python manage.py runserver 0.0.0.0:7777 &
	LASTPID=$!
	echo $LASTPID > HJKorean.pid
    ;;
    stop)
	echo "=========================================Stoping HJKorean Server============================================"
	CAMEROPID=$(cat /root/Camero/HJKorean.pid)
	echo $CAMEROPID
	pkill -9 -P $CAMEROPID
    ;;
esac
exit 0
