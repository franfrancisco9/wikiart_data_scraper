from utils import logger, get_artists_pages, get_artists_info

if __name__ == '__main__':
    logger.info('hello =)')
    csv_path = '/srv/data/alphabet_artists_pages.csv'
    get_artists_pages(csv_path)
    get_artists_info(csv_path, '/srv/data/artists_info.csv', '/srv/data/artists_wiki_texts.csv')