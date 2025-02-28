import { CheckCircle2 } from "lucide-react";
import React from "react";

const FilePreview = ({ upload }) => {
  return (
    <div className="mt-2 flex p-2 bg-slate-200 border rounded-md border-collapse items-center justify-between gap-2">
      <div className="flex items-center p-2">
        <CheckCircle2 className="mr-2 mt-1 fill-current text-[green] items-center" />
        <div className="text-left">
          <h2 className="">{upload.name}</h2>
          <h2 className="text-gray-400 text-[12px]">
            {upload?.type} / {(upload.size / 1024 / 1024).toFixed(2)}MB
          </h2>
        </div>
      </div>
    </div>
  );
};

export default FilePreview;
