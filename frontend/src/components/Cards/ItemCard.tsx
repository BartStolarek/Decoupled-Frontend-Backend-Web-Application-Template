// components/ItemCard.tsx
import React from 'react';

interface ItemCardProps {
    item: any;
    onButtonClick: (priceId: string, itemId: string) => void;
    buttonText: string;
}

const ItemCard: React.FC<ItemCardProps> = ({ item, onButtonClick, buttonText }) => {
    const formatPrice = (price: any) => {
        if (price && price.unit_amount) {
            return `$${(price.unit_amount / 100).toFixed(2)}`;
        }
        return 'Price not available';
    };

    return (
        <div className="card w-96 glass my-4">
            <figure>
                <img src={item.images[0]} alt={item.name} className="w-full h-48 object-cover" />
            </figure>
            <div className="card-body">
                <h2 className="card-title">{item.name}</h2>
                <p>{item.description}</p>
                <div className="card-actions justify-between items-center">
                    <div className="text-lg font-bold">
                        {item.display_price ? formatPrice(item.display_price) : formatPrice(item.default_price)}
                    </div>
                    <button
                        className="btn btn-primary"
                        onClick={() => onButtonClick(item.display_price.id, item.id)}
                    >
                        {buttonText}
                    </button>
                </div>
            </div>
        </div>
    );
};

export default ItemCard;