class constant:
	WINDOW_HEIGHT=24
	WINDOW_WIDTH=80
	BAT_SIZE=3
	DIFF_TRAJECTORY=False
	DIFF_SOUNDS=False
	MUSIC=False
	DIFF_SPEED=False

	esc = chr(27)
	#colors
	colorBlack   = chr(27)+"[40m "
	colorRed     = chr(27)+"[41m "
	colorGreen   = chr(27)+"[42m "
	colorYellow  = chr(27)+"[43m "
	colorBlue    = chr(27)+"[44m "
	colorMagenta = chr(27)+"[45m "
	colorCyan    = chr(27)+"[46m "
	colorWhite   = chr(27)+"[47m "

	#numbers
	zero =[
	esc+"[45m "+esc+"[45m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[45m "+esc+"[40m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[45m "+esc+"[40m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[45m "+esc+"[40m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[45m "+esc+"[45m "+esc+"[45m "+esc+"[1B"+esc+"[3D"]
	one =[
	esc+"[45m "+esc+"[45m "+esc+"[40m "+esc+"[1B"+esc+"[3D",
        esc+"[40m "+esc+"[45m "+esc+"[40m "+esc+"[1B"+esc+"[3D",
        esc+"[40m "+esc+"[45m "+esc+"[40m "+esc+"[1B"+esc+"[3D",
        esc+"[40m "+esc+"[45m "+esc+"[40m "+esc+"[1B"+esc+"[3D",
        esc+"[45m "+esc+"[45m "+esc+"[45m "+esc+"[1B"+esc+"[3D"]
	two =[
	esc+"[45m "+esc+"[45m "+esc+"[40m "+esc+"[1B"+esc+"[3D",
        esc+"[40m "+esc+"[40m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[40m "+esc+"[45m "+esc+"[40m "+esc+"[1B"+esc+"[3D",
        esc+"[45m "+esc+"[40m "+esc+"[40m "+esc+"[1B"+esc+"[3D",
        esc+"[45m "+esc+"[45m "+esc+"[45m "+esc+"[1B"+esc+"[3D"]
	three =[
	esc+"[45m "+esc+"[45m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[40m "+esc+"[40m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[45m "+esc+"[45m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[40m "+esc+"[40m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[45m "+esc+"[45m "+esc+"[45m "+esc+"[1B"+esc+"[3D"]
	four =[
	esc+"[45m "+esc+"[40m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[45m "+esc+"[40m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[45m "+esc+"[45m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[40m "+esc+"[40m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[40m "+esc+"[40m "+esc+"[45m "+esc+"[1B"+esc+"[3D"]
	five =[
	esc+"[45m "+esc+"[45m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[45m "+esc+"[40m "+esc+"[40m "+esc+"[1B"+esc+"[3D",
        esc+"[45m "+esc+"[45m "+esc+"[40m "+esc+"[1B"+esc+"[3D",
        esc+"[40m "+esc+"[40m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[45m "+esc+"[45m "+esc+"[40m "+esc+"[1B"+esc+"[3D"]
	six =[
	esc+"[45m "+esc+"[45m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[45m "+esc+"[40m "+esc+"[40m "+esc+"[1B"+esc+"[3D",
        esc+"[45m "+esc+"[45m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[45m "+esc+"[40m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[45m "+esc+"[45m "+esc+"[45m "+esc+"[1B"+esc+"[3D"]
	seven =[
	esc+"[45m "+esc+"[45m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[40m "+esc+"[40m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[40m "+esc+"[40m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[40m "+esc+"[40m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[40m "+esc+"[40m "+esc+"[45m "+esc+"[1B"+esc+"[3D"]
	eight =[
	esc+"[45m "+esc+"[45m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[45m "+esc+"[40m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[45m "+esc+"[45m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[45m "+esc+"[40m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[45m "+esc+"[45m "+esc+"[45m "+esc+"[1B"+esc+"[3D"]
	nine =[
	esc+"[45m "+esc+"[45m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[45m "+esc+"[40m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[45m "+esc+"[45m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[40m "+esc+"[40m "+esc+"[45m "+esc+"[1B"+esc+"[3D",
        esc+"[40m "+esc+"[40m "+esc+"[45m "+esc+"[1B"+esc+"[3D"]
