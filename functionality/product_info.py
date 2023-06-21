from models import session
from tables.product import SolarTable


def get_product_info(product_id):
    """
    This method is used to get product info using the product id
    :param product_id:
    :return: returning the dict of product information
    """
    if product_id:
        result = session.query(SolarTable).filter(
            SolarTable.id == product_id,
            SolarTable.is_deleted == 0
        ).first()
        if result:
            result_set = {"link": result.link, "id": result.id, "article_number": result.articleNumber,
                          "title": result.title, "breadcrums": result.breadcrums, "image": result.image}
        else:
            raise ValueError("No-Entry-Found")
    else:
        result = session.query(SolarTable).filter(
            SolarTable.is_deleted == 0
        ).all()

        result_array = []
        for product_ in result:
            temp_dict = dict()
            temp_dict["articleNumber"] = product_.articleNumber
            temp_dict["manufacturer_no"] = product_.articleNumber
            temp_dict["title"] = product_.title
            temp_dict["breadcrums"] = product_.breadcrums
            temp_dict["description"] = product_.description
            temp_dict["image"] = product_.image
            temp_dict["link"] = product_.link
            temp_dict["sitename"] = product_.sitename
            result_array.append(temp_dict)
        result_set = dict(result=result_array, status=True)
    return result_set
