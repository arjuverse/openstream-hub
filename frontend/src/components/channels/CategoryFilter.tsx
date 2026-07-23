import React from "react";

interface CategoryFilterProps {
  selectedCategory?: string;
  onSelectCategory: (category: string | undefined) => void;
}

export const CategoryFilter: React.FC<CategoryFilterProps> = ({ onSelectCategory }) => {
  return (
    <div className="flex gap-2 overflow-x-auto pb-2">
      <button 
        onClick={() => onSelectCategory(undefined)}
        className="px-4 py-2 text-sm bg-secondary rounded-md hover:bg-secondary/80"
      >
        All
      </button>
    </div>
  );
};