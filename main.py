import requests


def get_info_by_id(id: int) -> dict:
    try:
        url = "https://graph.infocasas.com.uy/graphql"
        query = """
            query GetProperty($id: ID!) {
              property(id: $id) {
                id
                title
                price {
                  amount
                  currency {
                    id
                    name
                    rate
                  }
                }
                link
              }
            }
            """
        headers = {
            "x-origin": "www.infocasas.com.uy",
            "Content-Type": "application/json",
        }

        response = requests.post(
            url, json={"query": query, "variables": {"id": id}}, headers=headers
        )
        response.raise_for_status()
        data = response.json()

        property_data = data["data"]["property"]

        title = property_data["title"]
        amount = property_data["price"]["amount"]
        currency_name = property_data["price"]["currency"]["name"]
        link = f'https://www.infocasas.com.uy/{property_data["link"]}'

        print(f'Title: {title}')
        print(f'Price: {amount} {currency_name}')
        print(f'More Info: {link}')
    except Exception as e:
        print(f'Price not found for id: {id}. ')


if __name__ == '__main__':
    try:
        prompt_id = int(input("Enter the id of the property: "))
        get_info_by_id(prompt_id)
    except Exception as e:
        print(f'Price not found for id: {id}. ')
