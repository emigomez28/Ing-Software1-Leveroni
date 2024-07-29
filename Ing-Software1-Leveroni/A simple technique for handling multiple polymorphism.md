
- Evitar código del tipo `if isKindOf:` 

- Una forma de manejar múltiple polimorfismo es haciendo un Double Disptach. Ej:  
	 `<Rectangle> displayOn: aPort` 
			`aPort displayRectangle: self`

- De esta forma se mantiene la modularidad y se mantiene un código extensible. 

- Ej de DD en los TPS en Servicios Financieros
		`<AccountTransaction<Deposit>>`
			`aceptar: unReporte`
				`unReporte visitarDeposito: self.`