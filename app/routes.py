from app import app, db
from .models import Gene
from flask import jsonify, request


@app.route("/")
def index():
    """
    Index page for the ensemble search portal
    :return welcome message
    """
    return "Welcome to the Ensemble Search Portal!"


@app.route("/gene_suggest")
def get_genes():
    """
    Endpoint to get gene names for the user query
    :return JSON returning all the gene names matching the user query
    """
    search = request.args.get("query")
    species = request.args.get("species")
    max_records = request.args.get("size")
    q = (
        db.session.query(Gene)
        .filter(Gene.species == species, Gene.display_label.startswith(search))
        .limit(max_records)
        .all()
    )

    format_query_op = dict(
        results=dict(
            species=species, query=search, geneNames=[gene.display_label for gene in q]
        )
    )

    resp = jsonify(format_query_op)
    return resp
