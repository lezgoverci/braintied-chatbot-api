def get_products(limit):
    return '''
    {{
        products(first: {0}) {{
            edges {{
                node {{
                    id
                    title
                    description
                    priceRange {{
                        minVariantPrice {{
                            amount
                        }}
                    }}
                }}
            }}
        }}
    }}'''.format(limit)