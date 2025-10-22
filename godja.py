import argparse

from app.core.client.httpClient import HttpClient
from app.core.payloads.base_payloads import BASE_PAYLOADS

method_attach_help = """
1 - GET With Query\n
2 - POST URL FORM\n
3 - POST JSON DATA\n
"""

v = 0.1

def show_banner(version: float) -> None:
    banner = f"""
     $$$$$$\                  $$\               
    $$  __$$\                 $$ |              
    $$ /  \__| $$$$$$\   $$$$$$$ |$$\  $$$$$$\  
    $$ |$$$$\ $$  __$$\ $$  __$$ |\__| \____$$\ 
    $$ |\_$$ |$$ /  $$ |$$ /  $$ |$$\  $$$$$$$ |
    $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |$$  __$$ |
    \$$$$$$  |\$$$$$$  |\$$$$$$$ |$$ |\$$$$$$$ |
     \______/  \______/  \_______|$$ | \_______| v{version}
                            $$\   $$ |          
                            \$$$$$$  |          
                             \______/"""
    print(banner)

def main():
    show_banner(v)
    parser = argparse.ArgumentParser()

    parser.add_argument("-u", "--url", help="target url")
    parser.add_argument("-m", "--method_attach", help=method_attach_help)

    args = parser.parse_args()

    client = HttpClient(
        url=args.url,
        payloads=BASE_PAYLOADS,
    )

    if args.method_attach == "1":
        ...
    elif args.method_attach == "2":
        client.ident_request_by_method_post_url_form()



if __name__ == "__main__":
    main()