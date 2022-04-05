const quotes = [
  {
    quote: "It is kind of fun to do the impossible.",
    author: "Walt Disney",
  },
  {
    quote: "I’ve failed over and over and over again in my life and that is why I succeed.",
    author: "Michael Jordan",
  },
  {
    quote: "If you run you stand a chance of losing, but if you don’t run you’ve already lost.",
    author: "Barack Obama",
  },
  {
    quote: "The greatest mistake you can make in life is to be continually fearing you will make one.",
    author: "Elbert Hubbard",
  },
  {
    quote: "To create more positive results in your life, replace ‘if only’ with ‘next time’.",
    author: "Unknown",
  },
  {
    quote: "They always say time changes things, but you actually have to change them yourself.",
    author: "Andy Warhol",
  },
  {
    quote: "Only I can change my life. No one can do it for me.",
    author: "Carol Burnett",
  },
  {
    quote: "We know what we are, but know not what we may be.",
    author: "William Shakespeare",
  },
  {
    quote: "What you have become is the price you paid to get what you used to want.",
    author: "Mignon McLaughlin",
  },
  {
    quote: "To improve is to change; to be perfect is to change often.",
    author: "Winston Churchill",
  },
];

const quote = document.querySelector("#quote span:first-child");
const author = document.querySelector("#quote span:last-child");

const todaysQuote = quotes[Math.floor(Math.random() * quotes.length)];

quote.innerText = todaysQuote.quote;
author.innerText = todaysQuote.author;
