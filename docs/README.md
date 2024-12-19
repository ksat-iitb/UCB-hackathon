# Web Search Agent

**Web Search Agent** is an intelligent system built with **Playwright** to automate web browsing tasks. This agent interacts with web pages by identifying and acting on interactive elements, such as buttons, links, and input fields. It now supports two modes of operation: using annotated screenshots with bounding boxes and utilizing the accessibility (a11y) tree, allowing for a more efficient web search experience without the need for visual processing. 

## Demo
https://github.com/user-attachments/assets/b8079314-d4d6-4ec2-a1f3-da5c1269f810

## Key Features

- **Interactive Element Detection:** The agent automatically detects and highlights interactive components like buttons, input fields, and links on a webpage, regardless of the method used (screenshot or a11y tree).

- **Dynamic Action Execution:** The agent executes a wide range of actions, including:
  - **Clicking** on buttons or links.
  - **Typing** into input fields.
  - **Scrolling** through web pages.
  - **Waiting** for content to load.
  - **Navigating** between web pages.
  It adapts its actions based on instructions and can execute the right task on the corresponding interactive element.

- **Accessibility Tree Integration:** With the newly added capability to utilize the accessibility tree, the agent can perform web searches without taking a screenshot. This allows for enhanced performance and reduced resource usage, making it suitable for a wider range of environments.

- **LLM-Based Decision Making:** Powered by a **Large Language Model (LLM)**, the agent analyzes the context of the web page and makes intelligent decisions on which actions to take, whether using the screenshot or a11y tree method.

- **Error Handling and Recovery:** The agent is capable of recovering from incorrect actions, such as clicking on the wrong element or missing interactions. It ensures precise actions even on pages with frequent layout changes.

- **Cross-Browser Compatibility:** The system works with multiple browser engines, including **Chromium**, **Firefox**, and **WebKit (Safari)**, thanks to Playwright’s cross-browser support. This ensures the agent can operate across a wide variety of platforms and environments.

- **Handling Dynamic Content:** The agent waits for all dynamic content to load before interacting, improving reliability on pages with delayed or asynchronous content loading.

## How It Works

1. **Screenshot & Annotation or A11y Tree Analysis:** The agent can either take a screenshot of the web page and label interactive elements with **bounding boxes** or analyze the accessibility tree to identify interactive components.

2. **Action Assignment:** The LLM processes the data (from either method) to identify which action (e.g., click, type, scroll) to perform based on the task.

3. **Interaction Execution:** The agent performs the instructed action on the correct interactive element.

4. **Result Evaluation:** After executing the action, the agent evaluates the result and adjusts its next steps, if necessary.

### Example Queries

#### Example: Find the distance between two places from Google Maps using screenshot

```plaintext
Enter your query: Can you tell me the distance from Bangalore to Singapore?
Thought: I will navigate to Google Maps to find the distance between Bangalore and Singapore.
Observation: Typed Singapore.
Thought: I will click on the "Directions" button to get the distance between Bangalore and Singapore.
Action Name: Click Tool
Action Input: {'label_number': 17}
Observation: Clicked the Button.
Thought: I will type "Bangalore" in the "Choose starting point, or click on the map" field to find the distance between Bangalore and Singapore.
Action Name: Type Tool
Action Input: {'label_number': 9, 'content': 'Bangalore'}
Observation: Typed Bangalore.
Thought: The screenshot shows the distance between Bangalore and Singapore is 4 hours and 40 minutes by flight.
Final Answer: The distance from Bangalore to Singapore is 4 hours and 40 minutes by flight.
```

#### Example: Weather of a place using a weather service by a11y tree

```plaintext
Enter your query: what is the weather in Bangalore from accuweather
Thought: I need to navigate to AccuWeather and search for the weather in Bangalore. I will use the GoTo Tool to navigate to the AccuWeather website.
Action Name: GoTo Tool
Action Input: {'url': 'https://www.accuweather.com/'}
Thought: The A11y Tree shows that the search box is now focused and the value is "Bangalore". I see a few options for "Bangalore" in the A11y Tree, but I need to click on the one that says "Bangalore, KA IN" to get the weather for Bangalore, India. I will use the Click Tool to select this option.
Action Name: Click Tool
Action Input: {'role': 'text', 'name': 'Bangalore, KA IN'}
Observation: Clicked the Button.
Thought: I have successfully navigated to the weather page for Bangalore, India. The A11y Tree shows the current temperature is 31°C. I can now provide the final answer.
Final Answer: The current temperature in Bangalore, India is 31°C.
```

#### Example: Price of a product from ecommerce website using combined (screenshoot + ally tree)
```plaintext
Enter your query: What is the price of iphone in amazon.in
Thought: The user wants to know the price of an iPhone on Amazon.in. I will navigate to Amazon.in and search for "iPhone" to find the relevant product listings.
Action Name: GoTo Tool
Action Input: {'url': 'https://www.amazon.in'}
Observation: Gone to https://www.amazon.in.
Thought: The A11y Tree shows a search box with the name "Search Amazon.in". I will type "iPhone" into the search box and click the "Go" button to search for iPhone products.
Action Name: Type Tool
Action Input: {'role': 'textbox', 'name': 'Search Amazon.in', 'content': 'iPhone'}
Observation: Typed iPhone.
Thought: The A11y Tree shows multiple iPhone models with their prices. I can provide the user with the prices of different iPhone models.
Final Answer: The price of iPhones on Amazon.in varies depending on the model and storage capacity. Here are some examples:

- **Apple iPhone 16 (128 GB) - White:** ₹xx,xxx
- **Apple iPhone 15 (128 GB) - Yellow:** ₹xx,xxx
- **Apple iPhone 13 (128GB) - Starlight:** ₹xx,xxx
- **Apple iPhone 16 Pro (256 GB) - Natural Titanium:** ₹xx,xxx
- **Apple iPhone 13 (128GB) - Midnight:** ₹xx,xxx
- **Apple iPhone 13 (128GB) - Pink:** ₹xx,xxx
- **Apple iPhone 16 Pro (512 GB) - White Titanium:** ₹xx,xxx
- **Apple iPhone 13 (128GB) - (Product) RED:** ₹xx,xxx
- **Apple iPhone 13 (128GB) - Blue:** ₹xx,xxx
- **Apple iPhone 16 (128 GB) - Black:** ₹xx,xxx
- **Apple iPhone 16 Pro (128 GB) - Desert Titanium:** ₹xx,xxx
- **Apple iPhone 15 (128 GB) - Blue:** ₹xx,xxx
- **Apple iPhone 13 (128GB) - Green:** ₹xx,xxx
- **Apple iPhone 15 (128 GB) - Black:** ₹xx,xxx
- **Apple iPhone 16 Pro (128 GB) - Black Titanium:** ₹xx,xxx
- **Apple iPhone 16 (128 GB) - Ultramarine:** ₹xx,xxx
- **Apple iPhone 13 (256GB) - Starlight:** ₹xx,xxx
- **Apple iPhone 14 (128 GB) - Blue:** ₹xx,xxx
```

## Installation

To set up the Web Search Agent, follow these steps:

1. Install Python 3.x and ensure it’s available in your environment.
2. Install project dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up **Playwright**:

   ```bash
   playwright install
   ```

## Usage

Once installed, you can choose between using the screenshot method or the accessibility tree method. The agent can be executed with the following command:

```bash
python app.py
```

## References

- **Playwright Documentation:** [https://playwright.dev/docs/intro](https://playwright.dev/docs/intro)
- **WebVoyager:** [https://github.com/MinorJerry/WebVoyager](https://github.com/MinorJerry/WebVoyager)
- **Langgraph Examples:** [https://github.com/langchain-ai/langgraph/blob/main/examples/web-navigation/web_voyager.ipynb](https://github.com/langchain-ai/langgraph/blob/main/examples/web-navigation/web_voyager.ipynb)
- **vimGPT:** [https://github.com/ishan0102/vimGPT](https://github.com/ishan0102/vimGPT)

---