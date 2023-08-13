class Person {

	constructor(name) {
	this.name = name;
	}

	introduce() {
	    console.log(`hello, my name is ${this.name} `);
	}

}

const otto = new Person('owesh');

otto.introduce();



