import React, { useState } from "react";

export function ToggleGroup({ children, type, value, onValueChange }) {
  const [selectedValue, setSelectedValue] = useState(value);

  const handleClick = (val) => {
    setSelectedValue(val);
    onValueChange(val);
  };

  return (
    <div className="flex space-x-2">
      {React.Children.map(children, (child) =>
        React.cloneElement(child, {
          isSelected: selectedValue === child.props.value,
          onClick: () => handleClick(child.props.value),
        })
      )}
    </div>
  );
}

export function ToggleGroupItem({ value, isSelected, onClick, children }) {
  return (
    <button
      className={`px-4 py-2 border rounded ${
        isSelected ? "bg-black text-white" : "bg-gray-200"
      }`}
      onClick={onClick}
    >
      {children}
    </button>
  );
}
