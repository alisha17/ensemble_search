from app import db


class Gene(db.Model):
    """
    Mapping for table 'gene_autocomplete'
    """

    __tablename__ = "gene_autocomplete"

    stable_id = db.Column(db.String(128), primary_key=True, nullable=False)
    species = db.Column(db.String(20))
    display_label = db.Column(db.String(128))
    location = db.Column(db.String(60))
    db = db.Column(db.String(32), nullable=False)
