import React from "react";
import Button from "./Button";

const Main = () => {
  return (
    <>
      <div className="container">
        <div className="p-5 text-center bg-light-dark rounded">
          <h1 className="text-light">Stock Prediction App</h1>
          <p className="text-light lead">
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. A deleniti
            perspiciatis vel obcaecati, excepturi numquam in facilis minus
            quisquam eveniet beatae fuga, velit debitis vitae alias quas ab!
            Architecto, ipsa.
          </p>

          <Button text={"Login"} class={"btn-outline-info"} link="/login" />
        </div>
      </div>
    </>
  );
};
export default Main;
