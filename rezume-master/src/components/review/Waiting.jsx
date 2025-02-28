import React from "react";

const Waiting = () => {
  return (
    <div className="text-center">
      <div className="flex flex-col items-center justify-center w-full ">
        <div className="w-[30%] mx-auto">
          <img src="/assets/waiting.gif" alt="Loading..." />{" "}
        </div>
        <h2 className="text-sm leading-6 items-center font-semibold flex justify-center text-center lg:w-[80%] w-[90%]">
          It can take upto 10 seconds
        </h2>
      </div>
    </div>
  );
};

export default Waiting;
