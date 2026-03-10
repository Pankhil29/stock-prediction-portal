import React from "react";

const Button = (props) => {
  return (
    <>
      <a href="" className={`btn ${props.class}`}>
        {props.text}
      </a>
    </>
  );
};

export default Button;

// anchor tag bydefault refresh the page, to thats why we use Router link component react-router-dom
