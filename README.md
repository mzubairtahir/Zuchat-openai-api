<h1>Zuchat 🤖</h1>

<p>This is a Python GUI application built with tkinter and customtkinter libraries that uses the OpenAI API to generate text. The user can copy the generated text through the copy button. The application consists of two files - <code>get.py</code> and <code>main.py</code>.</p>

<p><code>get.py</code> is responsible for sending requests to the OpenAI server and returning the generated text. <code>main.py</code> contains all the other code.</p>

<h2>Getting Started 🚀</h2>

<p>To use this application, you will need to have Python installed on your machine along with the following packages:</p>

<ul>
	<li>tkinter 🖥️</li>
	<li>openai 🤖</li>
	<li>customtkinter 🎨</li>
</ul>

<p>After installing Python and the required packages, you can clone this repository and run <code>main.py</code> to launch the application.</p>

<h2>Usage 🧑‍💻</h2>

<p>Once the application is launched, you can enter your prompt in the text field provided and click the "Submit" button. The generated text will be displayed in the text box below. You can then click the "Copy" button to copy the text to your clipboard.</p>

<p>The application is multi-threaded, which means that it will continue to respond even while the program is making requests to the OpenAI server. This ensures that the application remains responsive and doesn't freeze while generating text.</p>

<p>If you try to submit an empty prompt or a prompt with less than 3 characters, an error message will be displayed.</p>

<h2>Notes 📝</h2>

<p>This application is OOPs based, which makes it easy to extend and maintain. You can add new features or modify the existing ones by modifying the code in <code>main.py</code>.</p>

<h2>License 📜</h2>

<p>This project is licensed under the GPL v3.0 License - see the <code>LICENSE</code> file for details.</p>
