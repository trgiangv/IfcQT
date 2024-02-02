# read ifc file and extract information
import ifcopenshell
import ifcopenshell.util
import ifcopenshell.util.element
import ifcopenshell.util.selector
import ifcopenshell.util.selector


def get_info(ifc_file):
    ifc_file = ifcopenshell.open(ifc_file)
    products = ifc_file.by_type("IfcProduct")
    for product in products:
        print(product)
        print(product.is_a())
        print(product.GlobalId)
        print(product.Name)
        print(product.Description)
        print(product.ObjectType)
        print(product.ObjectPlacement)
        print(product.Representation)
        print(product.Decomposes)
        print(product.IsDecomposedBy)
        print(product.IsTypedBy)
        print(product.RelatingType)
        print(product.RelatedObjects)
        print(product.HasAssociations)
        print(product.Representation)
        print(product.IsDefinedBy)


def time_stamp(func):
    def wrapper(*args, **kwargs):
        import datetime
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        end = datetime.datetime.now()
        print(f"Time taken: {end - start}")
        return result

    return wrapper


@time_stamp
def get_info(ifc_file):
    ifc_file = ifcopenshell.open(ifc_file)
    products = ifc_file.by_type("IfcProduct")
    for product in products:
        print(product)
        print(product.is_a())
        print(product.GlobalId)
        print(product.Name)
        print(product.Description)
        print(product.ObjectType)
        print(product.ObjectPlacement)
        print(product.Representation)
        print(product.Decomposes)
        print(product.IsDecomposedBy)
        print(product.IsTypedBy)
        print(product.RelatingType)
        print(product.RelatedObjects)
        print(product.HasAssociations)
        print(product.Representation)
        print(product.IsDefinedBy)
