.thumb
.syntax unified

.include "gpio_constants.s"     // Register-adresser og konstanter for GPIO
.include "sys-tick_constants.s" // Register-adresser og konstanter for SysTick

.text
	.global Start
	
Start:

	LDR R0, =GPIO_BASE

	//SysTick
    //START SysTick
    LDR R5, =SYSTICK_BASE			//LOAD SysTick-ADR
    LDR R6, [R5]					//GET SysTick-VALUE
    ADD R6, R6, 0b110				//ADD 7 TO SysTick-VALUE
    STR R6, [R5]					//WRITE VALUE BACK TO SysTeck

    //SET CLOCKCYCLES
    LDR R6, =SYSTICK_LOAD			//Offset
    ADD R6, R6, R5					//Offset + SYSTICK_BASE
    LDR R7, =FREQUENCY/10			//Frequency (Hz)/10
    STR R7, [R6]

    //SET VAL WAIT
    LDR R6, =SYSTICK_VAL			//Offset
    ADD R6, R6, R5					//Offset + SYSTICK_BASE
    MOV R7, #0
    STR R7, [R6]					//Set wait to Freq/10

	//Interupt
	//SET PIN - EXTIPSELH
	LDR R4, =GPIO_EXTIPSELH			//Offset
	ADD R4, R4, R0					//Offset + GPIO_EXTIPSELLH
	MOV R5, 0b1111					//MAKE MASK
	LSL R5, R5, #4					//LEFTSHIFT MASK
	MVN R5, R5						//BITWISE NOT ON MASK
	AND R5, R5, R4					//AND ON MASK WITH ADR
	LDR R6, =PORT_B					//LOAD BUTTON PORT
	LSL R6, R6, #4					//LEFT-SHIFT TO MATCH REGISTER(PIN 9)
	ORR R6, R6, R5					//OR MASK WITH VALUE
	STR R6, [R4]					//WRITE BACK VALUE

	//EDIT EXTIFALL VALUE
	LDR R4, =GPIO_EXTIFALL			//Offset
	ADD R4, R4, R0					//Offset + GPIO_EXTIFALL
	LDR R5, [R4]					//LOAD GPIO_EXTIFALL-VALUE
	MOV R6, #1						//1
	LSL R6, R6, #9					//LEFTSHIFT TO GET CORRECT PLACEMENT
	ORR R6, R6, R5					//BITWISE OR ON GPIO_EXTIFALL-VALUE AND 1
	STR R6, [R4]					//WRITE VALUE BACK - CHECK FOR FALLING EDGE

	//SET IINTERUPT FLAG TO 0
	LDR R4, =GPIO_IFC				//Offset
	ADD R4, R4, R0					//Offset + GPIO_IFC
	MOV R5, #1						//1
	LSL R5, R5, #9					//LEFTSHIT TO GET CORRECT PLACEMENT
	STR R5, [R4]					//WRITE VALUE BACK TO RESET FLAG

	//START INTERUPT - INTERUPT ENABLE
	LDR R4, =GPIO_IEN 				//Offset
	ADD R4, R4, R0					//Offset + GPIO_EXTIFALL
	LDR R5, [R4]					//LOAD GPIO_EXTIFALL-VALUE
	MOV R6, #1						//1
	LSL R6, R6, #9					//LEFTSHIFT TO GET CORRECT PLACEMENT
	ORR R6, R6, R5					//BITWISE OR ON GPIO_EXTIFALL-VALUE AND 1
	STR R6, [R4]					//WRITE BACK VALUE - START INTERUPT

	//LED
	LDR R1, =36 					// 9w
	LDR R2, =PORT_E 				//LED
	LDR R3, =12 					// Offset
	MUL R4, R1, R2 					//9w * LED
	ADD R5, R4, R3 					// (9w * LED) + Offset
	ADD R6, R5, R0 					// (9w * LED) + Offset + GPIO_BASE
	LDR R7, [R6] 					//Get LED value

	//LED_clr
	LDR R3, =20
	MUL R4, R1, R2 					//9w * LED
	ADD R5, R4, R3 					// (9w * LED) + Offset
	ADD R12, R5, R0 				// (9w * LED) + Offset + GPIO_BASE

	//LED_tgl
	LDR R3, =GPIO_PORT_DOUTTGL

	MUL R4, R1, R2 					//9w * LED
	ADD R5, R4, R3					// (9w * LED) + Offset
	ADD R11, R5, R0 				// (9w * LED) + Offset + GPIO_BASE

	B LOOP

	LOOP:
		B LOOP

	.global SysTick_Handler
	.thumb_func
	SysTick_Handler:
		//USED REGISTERS

		//R0 = GPIO_BASE
		//R1 = TENTHS
		//R2 = SECONDS
		//R3 = MINUTES
		//R6 = LED_ADR
		//R7 = LED_VALUE
		//R11 = LED_TGL
		//R12 = LED_CLR

		LDR R1, =tenths
   		LDR R2, =seconds
    	LDR R3, =minutes


		COUNT_TENTHS:

		//COUNTING
    	LDR R8, [R1]				//GET TENTHS-VALUE
    	ADD R8, R8, #1				//ADD ONE TO CURRENT VALUE
    	STR R8, [R1]				//WRITE VALUE BACK TO TENTHS
    	CMP R8, #10					//COMPARE THENS-VALUE TO 10
    	BEQ COUNT_SECONDS			//BRANCH IF EQUAL -> SECONDS
    	BX LR

    	COUNT_SECONDS:
    	//LIGHT
    	MOV R5, #1
    	LSL R5, R5, #LED_PIN
		 				// Edit LED_value 2-nd bit to 1
		STR R5, [R11] 				// Write LED_value to LED_adr

    	MOV R12, #0
    	STR R12, [R1]

		//COUNTING
		LDR R9, [R2]				//GET SECONDS-VALUE
    	ADD R9, R9, #1				//ADD ONE TO CURRENT VALUE
    	STR R9, [R2]				//WRITE VALUE BACK TO SECOND

    	CMP R9, #60					//COMPARE SEC-VALUE TO 60
    	BEQ COUNT_MINUTES			//BRANCH IF EQUAL -> MINUTES
    	BX LR

    	COUNT_MINUTES:
    	STR R12, [R2]				//RESET SECONDS TO 0

    	LDR R10, [R3]				//GET MINUTES-VALUE
    	ADD R10, R10, #1			//ADD ONE TO CURRENT VALUE
    	STR R10, [R3]				//WRITE VALUE BACK TO MINUTES
    	BX LR

	.global GPIO_ODD_IRQHandler
	.thumb_func
	GPIO_ODD_IRQHandler:

		LDR R4, =SYSTICK_BASE
		LDR R5, [R4]
		EOR R5, R5, #1
		STR R5, [R4]


		//SET IINTERUPT FLAG TO 0
		LDR R4, =GPIO_IFC			//Offset
		ADD R4, R4, R0				//Offset + GPIO_IFC
		MOV R5, #1					//1
		LSL R5, R5, #9				//LEFTSHIT TO GET CORRECT PLACEMENT
		STR R5, [R4]				//WRITE VALUE BACK TO RESET FLAG

		BX LR //returnerer fra interupt


NOP // Behold denne på bunnen av fila