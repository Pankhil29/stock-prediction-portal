import React from "react";
import Button from "./Button";
import { Link } from "react-router-dom";

const Header = () => {
  return (
    <>
      <nav className="navbar container pt-3 pb-3 align-items-start">
        <Link to="/" className="navbar-brand text-light">
          Stock Prediction Portal
        </Link>
        <div>
          <Button text={"Login"} class={" btn-outline-info"} link="/login" />
          &nbsp;
          <Button text={"Register"} class={" btn-info"} link="/register" />
        </div>
      </nav>
    </>
  );
};

export default Header;
