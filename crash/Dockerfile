FROM ruby:2.7.2-slim

# install rails dependencies
RUN apt-get clean all && apt-get update -qq && apt-get -y upgrade && apt-get install -y build-essential libpq-dev \
    curl gnupg2 apt-utils default-libmysqlclient-dev git libcurl3-dev cmake \
    libssl-dev pkg-config openssl imagemagick file nodejs yarn libpq-dev

ENV APP /usr/src/app
RUN mkdir $APP
WORKDIR $APP
COPY Gemfile* $APP/

RUN gem install bundler -v '2.3.22'
RUN gem update --system 3.2.3
ENV BUNDLER_VERSION=2.3.22
RUN bundle install

COPY . $APP/

EXPOSE 3000
# RUN bundle exec rake db:migrate db:seed
CMD ["bundle", "exec", "puma", "-C", "config/puma.rb"]
