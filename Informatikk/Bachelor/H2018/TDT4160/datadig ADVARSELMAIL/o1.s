.thumb
.syntax unified

.include "gpio_constants.s"     // Register-adresser og konstanter for GPIO

.text
	.global Start
	
Start:

	LDR R0, =GPIO_BASE
	LDR R1, =36 // 9w

	//LED
	LDR R2, =PORT_E //LED
	LDR R3, =12 // Offset

	MUL R4, R1, R2 //9w * LED
	ADD R5, R4, R3 // (9w * LED) + Offset
	ADD R6, R5, R0 // (9w * LED) + Offset + GPIO_BASE
	//R6 = LED_adr

	LDR R7, [R6] //Get LED value
	//R7 = LED_value

	//LED_clr
	LDR R3, =20

	MUL R4, R1, R2 //9w * LED
	ADD R5, R4, R3 // (9w * LED) + Offset
	ADD R10, R5, R0 // (9w * LED) + Offset + GPIO_BASE
	//R10 = LED_clr

	//LED_tgl
	LDR R3, =24

	MUL R4, R1, R2 //9w * LED
	ADD R5, R4, R3 // (9w * LED) + Offset
	ADD R11, R5, R0 // (9w * LED) + Offset + GPIO_BASE
	//R11 = LED_tgl

	//BUTTON
	LDR R2, =PORT_B //BUTTON
	LDR R3, =28 // Offset

	MUL R4, R1, R2 //9w * BUTTON
	ADD R5, R4, R3 // (9w * BUTTON) + Offset
	ADD R8, R5, R0 // (9w * BUTTON) + Offset + GPIO_BASE
	//R8 = BUTTON_adr

	MOV R0, 4 //Save bit number (2) for CLR and TGL

	//R0 = LED bit number
	//R6 = LED_adr
	//R7 = LED_value
	//R10 = LED_clr
	//R11 = LED_tgl
	//R8 = BUTTON_adr
	//R9 = BUTTON_value
	//B NOLIGHT
	//B LOOP

	LOOP:
	//Get BUTTON value
	LDR R9, [R8] //Get BUTTON value

	CMP R9, 512 //Check button state, set Z-flag
	//IF branch NOLIGHT
	BEQ NOLIGHT
	//ELSE
	B LIGHT

	NOLIGHT:
	STR R0, [R10] //Set bit two -> 0
	B LOOP

	LIGHT:
	ORR R11, R7, 4
	STR R11, [R6]
	B LOOP

NOP // Behold denne på bunnen av fila