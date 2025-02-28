import React from "react";

const Strength = ({ answer }) => {
  const feedback = () => {
    if (answer > 80) return "Outstanding Resume";
    else if (answer > 70) return "Good Resume";
    else if (answer > 50) return "Average Resume";
    else return " Resume needs Improvement";
  };
  return (
    <div className="text-center">
      <div className="flex flex-col items-center justify-center w-full gap-8">
        <h2 className="text-3xl font-bold md:text-left text-center">
          Relevance <span className="text-primary">Strength </span>
        </h2>

        <div className="rounded-[50%] w-32 h-32 border-primary border-4 flex items-center  justify-center text-lg font-bold">
          {answer ? answer : "error"}
        </div>

        <p
          className={`text-base leading-6 items-center font-semibold flex justify-center text-center lg:w-[80%] w-[90%]  ${
            answer > 50 ? "text-[#130e49]" : "text-[red]"
          }`}
        >
          {feedback()}
        </p>
      </div>
    </div>
  );
};

export default Strength;
