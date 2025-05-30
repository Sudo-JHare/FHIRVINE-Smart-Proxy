"""Create initial schema after purge

Revision ID: 4e8d36d8e416
Revises: 
Create Date: 2025-04-23 13:08:11.515425

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e8d36d8e416'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('configurations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('key', sa.String(length=100), nullable=False),
    sa.Column('value', sa.Text(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('last_updated', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('key')
    )
    op.create_table('oauth_tokens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.String(length=100), nullable=False),
    sa.Column('token_type', sa.String(length=40), nullable=True),
    sa.Column('access_token', sa.String(length=255), nullable=False),
    sa.Column('refresh_token', sa.String(length=255), nullable=True),
    sa.Column('scope', sa.Text(), nullable=True),
    sa.Column('issued_at', sa.Integer(), nullable=False),
    sa.Column('expires_in', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('registered_apps',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('app_name', sa.String(length=100), nullable=False),
    sa.Column('client_id', sa.String(length=100), nullable=False),
    sa.Column('client_secret_hash', sa.String(length=200), nullable=False),
    sa.Column('redirect_uris', sa.Text(), nullable=False),
    sa.Column('scopes', sa.Text(), nullable=False),
    sa.Column('logo_uri', sa.String(length=255), nullable=True),
    sa.Column('contacts', sa.Text(), nullable=True),
    sa.Column('tos_uri', sa.String(length=255), nullable=True),
    sa.Column('policy_uri', sa.String(length=255), nullable=True),
    sa.Column('jwks_uri', sa.String(length=255), nullable=True),
    sa.Column('date_registered', sa.DateTime(), nullable=True),
    sa.Column('last_updated', sa.DateTime(), nullable=True),
    sa.Column('is_test_app', sa.Boolean(), nullable=True),
    sa.Column('test_app_expires_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('app_name'),
    sa.UniqueConstraint('client_id')
    )
    op.create_table('authorization_codes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=255), nullable=False),
    sa.Column('client_id', sa.String(length=100), nullable=False),
    sa.Column('redirect_uri', sa.Text(), nullable=True),
    sa.Column('scope', sa.Text(), nullable=True),
    sa.Column('nonce', sa.String(length=255), nullable=True),
    sa.Column('code_challenge', sa.String(length=255), nullable=True),
    sa.Column('code_challenge_method', sa.String(length=10), nullable=True),
    sa.Column('response_type', sa.String(length=40), nullable=True),
    sa.Column('state', sa.String(length=255), nullable=True),
    sa.Column('issued_at', sa.Integer(), nullable=False),
    sa.Column('expires_at', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['registered_apps.client_id'], name='fk_authorization_codes_client_id'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('authorization_codes')
    op.drop_table('registered_apps')
    op.drop_table('oauth_tokens')
    op.drop_table('configurations')
    # ### end Alembic commands ###
