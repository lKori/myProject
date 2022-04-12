import React from "react";
// import ReactDOM from "react-dom";

function App() {
    const [counter, setCounter] = React.useState(0);
    const onClick = () => {
        setCounter(counter + 1);
    };
    return (
        <div>
            <h3>Total clicks: {counter}</h3>
            <button onClick={onClick}>Click me</button>
        </div>
    );
}

export default App;
